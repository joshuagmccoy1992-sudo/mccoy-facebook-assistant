#!/usr/bin/env bash
set -euo pipefail
# Install on an Ubuntu/Debian desktop or VM under a normal non-root user.
command -v python3 >/dev/null || { echo "Python 3 required"; exit 1; }
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r browser_agent/requirements.txt
.venv/bin/python -m playwright install chromium
mkdir -p "$HOME/.mccoy-browser"
chmod 700 "$HOME/.mccoy-browser"
ROOT="$(pwd)"
PY="$ROOT/.venv/bin/python"
JOB="$ROOT/browser_agent/agent.py"
LOG="$HOME/mccoy-browser.log"
( crontab -l 2>/dev/null | grep -v 'browser_agent/agent.py' || true
  printf '0 * * * * MCCOY_HEADLESS=true %s %s >> %s 2>&1\n' "$PY" "$JOB" "$LOG"
) | crontab -
echo "Installed hourly browser health-check. Login must be completed by owner in visible browser before unattended use."
echo "No automated Facebook posting/commenting is installed."
