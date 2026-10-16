# Persistent browser agent (prototype)

This is a **real runnable browser health-check**, not a deployed Facebook group bot. It launches Chromium with a reusable browser profile in a private directory, visits Facebook, records whether the page loaded, and closes the browser without deleting its profile. It does not log in, comment, post, or bypass challenges. Login status is only a heuristic.

## Run on an owned desktop/VM

Install Python 3.12+, then:

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r browser_agent/requirements.txt
python -m playwright install chromium
python browser_agent/agent.py
```

For first login, open the persistent profile in a visible desktop browser and authenticate yourself. Do not send a password to ChatGPT or commit credentials to GitHub. The private profile is stored under `~/.mccoy-browser` unless `MCCOY_BROWSER_DATA` is set. Keep the profile out of shared storage. The agent intentionally does not automate login.

## Hourly schedule (Linux cron)

```cron
0 * * * * cd /path/to/repo && /path/to/repo/.venv/bin/python browser_agent/agent.py >> /home/USER/mccoy-agent.log 2>&1
```

This only schedules the health check; it does not run until installed on a real machine. A graphical session may be required because the default is headful. Set `MCCOY_HEADLESS=true` for background execution after interactive login, but Facebook may still require verification.

## Next integration

Add read-only checks of specifically approved business destinations, deduplication and permission checks; integrate approved posting only after a verified authenticated mechanism exists. Store secrets/profile only on the VM, never in the public repository.
