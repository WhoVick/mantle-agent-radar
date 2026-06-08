import argparse
import asyncio
import json
import os
from datetime import timezone
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from dotenv import load_dotenv
from telethon import TelegramClient, events


def env(name: str, default: str | None = None) -> str:
    value = os.getenv(name, default)
    if value is None or value == "":
        raise SystemExit(f"Missing required env var: {name}")
    return value


def parse_chats(raw: str) -> list[str]:
    chats = [item.strip() for item in raw.split(",")]
    return [item for item in chats if item]


def parse_proxy(raw: str | None) -> tuple[Any, str, int, bool, str | None, str | None] | None:
    if raw is None or raw.strip() == "":
        return None

    parsed = urlparse(raw.strip())
    if parsed.scheme == "" or parsed.hostname is None or parsed.port is None:
        raise SystemExit("TELEGRAM_PROXY must look like socks5://user:pass@host:port")

    try:
        import socks
    except ImportError as exc:
        raise SystemExit("Install PySocks to use TELEGRAM_PROXY: python -m pip install PySocks") from exc

    scheme = parsed.scheme.lower()
    proxy_types = {
        "socks4": socks.SOCKS4,
        "socks5": socks.SOCKS5,
        "socks5h": socks.SOCKS5,
        "http": socks.HTTP,
        "https": socks.HTTP,
    }
    if scheme not in proxy_types:
        raise SystemExit("TELEGRAM_PROXY scheme must be socks4, socks5, socks5h, http, or https")

    username = unquote(parsed.username) if parsed.username else None
    password = unquote(parsed.password) if parsed.password else None
    return (proxy_types[scheme], parsed.hostname, parsed.port, scheme == "socks5h", username, password)


def iso_date(value: Any) -> str | None:
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat()


def message_to_record(message: Any, chat: Any) -> dict[str, Any]:
    sender = getattr(message, "sender_id", None)
    text = message.message or ""
    return {
        "message_id": message.id,
        "date_utc": iso_date(message.date),
        "chat_id": getattr(chat, "id", None),
        "chat_title": getattr(chat, "title", None) or getattr(chat, "username", None),
        "sender_id": sender,
        "text": text,
        "has_media": bool(getattr(message, "media", None)),
        "reply_to_msg_id": getattr(message, "reply_to_msg_id", None),
    }


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


async def fetch_history(client: TelegramClient, chats: list[str], output: Path, limit: int) -> None:
    if limit <= 0:
        return
    for chat_ref in chats:
        entity = await client.get_entity(chat_ref)
        messages = []
        async for message in client.iter_messages(entity, limit=limit):
            messages.append(message)
        for message in reversed(messages):
            append_jsonl(output, message_to_record(message, entity))
        print(f"Fetched {len(messages)} history messages from {chat_ref}")


async def main() -> None:
    parser = argparse.ArgumentParser(description="Listen to Telegram chats and save messages as JSONL.")
    parser.add_argument("--history", type=int, default=0, help="Fetch the last N messages before listening.")
    args = parser.parse_args()

    load_dotenv()

    api_id = int(env("TG_API_ID"))
    api_hash = env("TG_API_HASH")
    phone = env("TG_PHONE")
    chats = parse_chats(env("TG_CHATS"))
    session = env("TG_SESSION", "sessions/mantle_hackathon")
    output = Path(env("TG_OUTPUT", "data/telegram_messages.jsonl"))
    proxy = parse_proxy(os.getenv("TELEGRAM_PROXY"))

    Path(session).parent.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)

    client = TelegramClient(session, api_id, api_hash, proxy=proxy)
    await client.start(phone=phone)

    entities = [await client.get_entity(chat_ref) for chat_ref in chats]
    await fetch_history(client, chats, output, args.history)

    @client.on(events.NewMessage(chats=entities))
    async def handler(event: events.NewMessage.Event) -> None:
        chat = await event.get_chat()
        record = message_to_record(event.message, chat)
        append_jsonl(output, record)
        preview = record["text"].replace("\n", " ")[:160]
        print(f"[{record['date_utc']}] {record['chat_title']}: {preview}")

    print("Listening for new Telegram messages. Press Ctrl+C to stop.")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
