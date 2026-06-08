$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectDir = Split-Path -Parent $ScriptDir
$Python = Join-Path $ProjectDir ".venv\Scripts\python.exe"
$EnvPath = Join-Path $ScriptDir ".env"

if (-not (Test-Path -LiteralPath $Python)) {
    throw "Python venv not found at $Python"
}

Push-Location $ScriptDir
try {
    if (-not (Test-Path -LiteralPath $EnvPath)) {
        & (Join-Path $ScriptDir "setup_env.ps1")
    }
    & $Python listen.py --history 200
}
finally {
    Pop-Location
}
