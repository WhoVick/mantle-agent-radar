# Telegram Monitor

Read-only Telegram monitor for Mantle hackathon intelligence.

## Setup

1. Create a Telegram app at https://my.telegram.org/apps.
2. Copy `.env.example` to `.env`.
3. Fill `TG_API_ID`, `TG_API_HASH`, `TG_PHONE`, `TG_CHATS`.
   If Telegram must use a proxy, set `TELEGRAM_PROXY` in URL form:

```dotenv
TELEGRAM_PROXY=socks5://user:password@host:port
```

   Or run:

```powershell
.\setup_env.ps1
```

4. Install dependencies from the project root:

```powershell
..\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

5. Run:

```powershell
..\.venv\Scripts\python.exe listen.py --history 200
```

On first run Telethon will ask for the login code sent to Telegram and, if enabled, the 2FA password. Do not paste those into shared chat; enter them only in the local terminal.

## Output

Messages are appended to `data/telegram_messages.jsonl`.
