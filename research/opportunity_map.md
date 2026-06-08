# Opportunity Map

## Главное ограничение

На 2026-06-08 по самым надежным публичным источникам осталось около недели до 2026-06-15. Есть конфликтующий Luma-источник с 2026-07-15, но пока это нельзя считать основным дедлайном. С высокой вероятностью выиграет не самый "глубокий" код, а проект, который:

- точно попадает в один трек;
- имеет живой demo flow;
- использует Mantle не декоративно;
- показывает agent decision log;
- объясняет, как из этого получается value.

## Выбранный путь: Mantle Agent Radar

**Трек:** AI Alpha & Data, Mirana Ventures.

**Что делает:** агент читает Telegram/Discord/X и on-chain события Mantle, выделяет alpha/anomaly/risk signals, объясняет источник сигнала, присваивает confidence, пишет hash/attestation решения on-chain и показывает dashboard.

**Почему это хороший шанс:**

- Трек прямо упоминает Telegram/Discord bots и anomaly detection.
- Judging sheet дает 15 баллов за insight value, 15 за data source quality, 12 за investment utility, 8 за scalability.
- Нам не нужно торговать реальными средствами, чтобы показать ценность.
- Можно быстро сделать MVP на Python + dashboard.
- Есть понятная коммерческая версия: paid alerts для фондов/трейдеров/market makers.
- В чате уже видно, что конкуренты толпятся вокруг RWA vaults, agent reputation и generic backtests; investor-grade Mantle intelligence выглядит менее забитой нишей.

**MVP за неделю:**

1. Telegram listener собирает сообщения из hackathon/Mantle/alpha чатов в JSONL.
2. Signal engine классифицирует сообщения: alpha, rumor, integration, deadline, technical help, risk.
3. On-chain watcher подтягивает простые Mantle события: transfers/swaps/contract calls по избранным адресам/protocols.
4. Scoring: novelty, source credibility, cross-source confirmation, on-chain confirmation, urgency.
5. Dashboard: signals, evidence, confidence, agent action log.
6. On-chain proof: contract или минимальная запись hash(signal payload) + timestamp + agent id.

**Pitch:** "We turn noisy social and Mantle-native on-chain streams into verifiable investor-grade alpha, with every signal explainable and attestable."

## Второй путь: Mantle Agent Audit Copilot

**Трек:** AI DevTools.

**Что делает:** проверяет Solidity/agent configs для Mantle: gas pitfalls, unsafe approvals, missing slippage, oracle risk, unbounded agent permissions, missing kill switch.

**Почему может выиграть:**

- Судьи любят tooling, потому что оно полезно всему ecosystem.
- Быстрее сделать, чем полноценную trading стратегию.
- Можно показать до/после на demo contracts.

**Риск:** нужен хороший набор Mantle-specific checks, иначе будет выглядеть как обычный LLM-аудитор.

## Третий путь: RWA Risk/Yield Agent

**Трек:** AI x RWA.

**Что делает:** агент выбирает allocation между mETH/USDY/другими Mantle RWA/yield активами, учитывая APY, liquidity, depeg/oracle risk, gas, drawdown.

**Почему денежно:** Mantle активно позиционирует себя как bridge к TradFi/RWA. Это близко к нарративу спонсоров.

**Риск:** нужно больше DeFi-интеграций и аккуратных данных, а времени мало. Конкуренты уже, вероятно, делают "yield router" проекты.

## Как заработать

### Прямо на хакатоне

- Целиться в Phase 2 prize pool $100,000.
- Не распыляться по трекам: выбрать AI Alpha & Data или AI DevTools.
- Сделать сильную demo story: live input -> agent decision -> on-chain proof -> dashboard -> measurable value.
- В Telegram-чате быстро уточнить критерии, требуемые артефакты и sponsor-specific prizes.

### После хакатона

1. **B2B signals subscription**: $99-$999/month для трейдеров, small funds, DAO treasuries.
2. **Custom intelligence bot** для проектов Mantle: paid setup + monthly monitoring.
3. **Grant/follow-on funding**: Mantle ecosystem, Bybit/Byreal, HackQuest/DoraHacks visibility.
4. **Open-source core + paid hosted dashboard**: лучший баланс для хакатона, потому что open-source повышает доверие судей.
5. **Affiliate/referral integrations**: если продукт идет в trading/alerts, можно монетизировать через биржевые/API партнерки, но в заявке лучше не делать это центральным тезисом.

## План на 7 дней

### Day 1

- Подключить Telegram-monitor.
- Собрать последние сообщения из хакатон-чата.
- Уточнить submission requirements.
- Выбрать финальный трек.

### Day 2-3

- Сделать ingestion pipeline.
- Добавить LLM/scoring слой.
- Подготовить простые on-chain Mantle data inputs.

### Day 4

- Сделать dashboard.
- Добавить agent action log и evidence view.

### Day 5

- Добавить on-chain attestation/proof.
- Подготовить demo сценарии.

### Day 6

- Записать demo video.
- Полировать README, architecture diagram, pitch.

### Day 7

- Финальная DoraHacks submission.
- Пост в Telegram/X, собрать реакцию, попросить feedback у организаторов.

## Что нужно уточнить в Telegram-чате

- Точный submission deadline и timezone.
- Что именно означает конфликт June 15/16 vs July 15.
- Можно ли подавать solo/team и ограничения по team size.
- Нужен ли deployed contract на Mantle mainnet/testnet.
- Дают ли templates для Python/Solidity/Byreal Skills CLI.
- Требуется ли ERC-8004 строго или достаточно compatible identity/proof.
- Есть ли sponsor prizes по Nansen/Elfa/Bybit/Byreal/Tencent Cloud.
- Формат demo: видео, GitHub, live URL, smart contract address.
