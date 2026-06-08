# Runbook

## Rebuild Signals

```powershell
cd D:\Correlations_in_the_Russian_fund_Claude\Mantle_Turing_Test_Hackathon_2026
.\.venv\Scripts\python.exe -m agent_radar.build_signals
```

## Open Dashboard

Open:

```text
D:\Correlations_in_the_Russian_fund_Claude\Mantle_Turing_Test_Hackathon_2026\web\index.html
```

The dashboard is static and uses `web\data\signals.js`, so it works from a normal browser without a backend.

## Validate

```powershell
.\.venv\Scripts\python.exe -m py_compile agent_radar\models.py agent_radar\scoring.py agent_radar\build_signals.py
node --check web\app.js
```

## Telegram

Current active browser session is logged into Telegram Web. Use the visible browser for manual chat monitoring. The Telethon monitor is still available in `telegram_monitor/` if API credentials are later provided.

## Submission Assets

- `research\telegram_intel.md`
- `research\winning_strategy.md`
- `submission\dorahacks_copy.md`
- `submission\demo_script.md`
- `contracts\SignalRegistry.sol`

