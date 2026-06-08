# Telegram Monitoring Plan

Цель: читать официальный Telegram-чат хакатона в реальном времени и превращать сообщения в actionable intelligence: дедлайны, уточнения правил, ссылки на templates, вопросы участников, идеи конкурентов, сигналы от организаторов.

Чат: https://t.me/MantleTuringTestHackathon

Проверка 2026-06-08: Telegram web показывает группу **Mantle The Turing Test Hackathon**, 255 members, 42 online. Сообщения через публичную web-страницу не видны, поэтому нужен user-client.

## Безопасный вариант

Используем отдельный Telegram-аккаунт и Telethon user client.

Что понадобится локально:

- `TG_API_ID` и `TG_API_HASH` из https://my.telegram.org/apps
- номер телефона отдельного аккаунта;
- ссылка/username чата хакатона;
- одноразовый Telegram login code при первом запуске;
- 2FA password, если включен.

Важно: код входа и пароль не нужно присылать в чат Codex. Их лучше вводить локально в терминале при первом запуске.

## Почему не Telegram Bot API

Bot API часто не подходит: бота нужно добавить в чат, у него могут быть ограничения на чтение истории/сообщений, а публичные/полупубличные хакатон-чаты часто не дают ботам полный доступ. User client надежнее для read-only monitoring, если это не нарушает правила чата.

## Что уже подготовлено

В папке `telegram_monitor/` лежит минимальный listener:

- читает `.env`;
- подключается к указанным чатам;
- при запуске может забрать последние N сообщений;
- пишет новые сообщения в `data/telegram_messages.jsonl`;
- не коммитит `.env`, session files и data logs.

## Что сделать после получения аккаунта

1. Скопировать `telegram_monitor/.env.example` в `telegram_monitor/.env`.
2. Заполнить `TG_API_ID`, `TG_API_HASH`, `TG_PHONE`, `TG_CHATS`.
3. Установить зависимости:

```powershell
python -m pip install -r telegram_monitor\requirements.txt
```

4. Первый запуск:

```powershell
python telegram_monitor\listen.py --history 200
```

5. Дальше оставить процесс запущенным для real-time capture.

## Что я буду извлекать из чата

- official announcements;
- deadline changes;
- organizer answers;
- sponsor links/templates;
- judge preferences;
- common participant blockers;
- competitor direction signals;
- bounty/special prize hints.
