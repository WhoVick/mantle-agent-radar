$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$EnvPath = Join-Path $ScriptDir ".env"

Write-Host "Telegram user-client setup for Mantle hackathon monitor"
Write-Host "Create API credentials at https://my.telegram.org/apps first."
Write-Host ""

$ApiId = Read-Host "TG_API_ID"
$ApiHash = Read-Host "TG_API_HASH"
$Phone = Read-Host "TG_PHONE, with country code"

$Content = @"
TG_API_ID=$ApiId
TG_API_HASH=$ApiHash
TG_PHONE=$Phone
TG_CHATS=https://t.me/MantleTuringTestHackathon
TG_SESSION=sessions/mantle_hackathon
TG_OUTPUT=data/telegram_messages.jsonl
"@

Set-Content -LiteralPath $EnvPath -Value $Content -Encoding UTF8
Write-Host "Wrote $EnvPath"

