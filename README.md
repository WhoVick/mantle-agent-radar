# Mantle Turing Test Hackathon 2026

Рабочая папка для разведки и подготовки заявки на Mantle Turing Test Hackathon 2026.

## Текущий вывод

Сегодня 2026-06-08. Phase 2, AI Awakening, идет примерно до 2026-06-15/16, поэтому у нас около недели. Оптимальная стратегия - не пытаться выиграть чистый trading contest, а собрать убедительный AI agent product в одном из менее перегретых треков:

1. **AI Alpha & Data** - лучший шанс для нас, потому что можно использовать наши сильные стороны: real-time Telegram/social intelligence, on-chain anomaly detection, сигналы, объяснимые алерты.
2. **AI DevTools** - второй хороший путь: Mantle-specific audit/gas/risk assistant для агентских кошельков и smart contracts.
3. **AI x RWA** - потенциально самый "денежный" и близкий к теме Mantle, но требует аккуратной DeFi/RWA интеграции.

Рекомендованная идея: **Mantle Agent Radar** - AI-агент, который читает Telegram/Discord/X и on-chain данные Mantle, находит alpha/anomaly/risk signals, записывает решения/сигналы в on-chain trace, показывает dashboard и имеет ERC-8004-like agent identity/reputation layer.

## Файлы

- [research/hackathon_brief.md](research/hackathon_brief.md) - что за хакатон, сроки, треки, критерии.
- [research/opportunity_map.md](research/opportunity_map.md) - что строить, как повышать шанс на приз, как заработать после хакатона.
- [research/telegram_monitoring.md](research/telegram_monitoring.md) - как подключить Telegram-чат хакатона и читать его в реальном времени.
- [research/telegram_intel.md](research/telegram_intel.md) - реальные сигналы из Telegram/DevHub/criteria sheet после авторизации.
- [research/winning_strategy.md](research/winning_strategy.md) - выбранная стратегия под scoring и деньги.
- [telegram_monitor/](telegram_monitor/) - заготовка Telethon-монитора для Telegram.
- [web/index.html](web/index.html) - MVP dashboard.
- [contracts/SignalRegistry.sol](contracts/SignalRegistry.sol) - on-chain proof contract.
- [submission/dorahacks_copy.md](submission/dorahacks_copy.md) - черновик заявки.
- [submission/x_thread.md](submission/x_thread.md) - черновик X-thread под Community Voting.
- [submission/mainnet_deployment_plan.md](submission/mainnet_deployment_plan.md) - план быстрого mainnet deployment.
- [RUNBOOK.md](RUNBOOK.md) - команды запуска и проверки.
- [JUDGES.md](JUDGES.md) - краткий файл для судей.
- [DEPLOYMENT.md](DEPLOYMENT.md) - публичный dashboard и Mantle deployment.

## Ближайшие действия

1. Собрать MVP `Mantle Agent Radar`.
2. Подать в Track 02, **AI Alpha & Data**.
3. Развернуть proof/registry contract на Mantle mainnet, если успеваем; иначе testnet с четкой mainnet-инструкцией.
4. Подготовить X-thread для Community Voting.

## Commands

```powershell
python -m agent_radar.build_signals
npm run check
npm run hash:top
```
