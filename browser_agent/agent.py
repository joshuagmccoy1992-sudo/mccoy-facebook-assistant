"""Persistent, owner-authenticated browser for McCoy Carpentry.
Read-only connectivity/health check. Does NOT automate Facebook comments.
Run on a computer/VM with a desktop and a persistent private data directory.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(os.environ.get("MCCOY_BROWSER_DATA", str(Path.home() / ".mccoy-browser"))).expanduser()
REPORT = Path(os.environ.get("MCCOY_REPORT_PATH", str(Path.home() / "mccoy-browser-status.json"))).expanduser()
URL = "https://www.facebook.com/"
HEADLESS = os.environ.get("MCCOY_HEADLESS", "false").lower() == "true"

def run():
    BASE.mkdir(mode=0o700, parents=True, exist_ok=True)
    result = {"checked_at": datetime.now(timezone.utc).isoformat(), "site": URL,
              "browser_started": False, "facebook_loaded": False,
              "login_status": "unknown", "error": None}
    try:
        with sync_playwright() as p:
            context = p.chromium.launch_persistent_context(
                str(BASE), headless=HEADLESS, channel=os.environ.get("MCCOY_BROWSER_CHANNEL") or None,
                viewport={"width": 1280, "height": 850},
            )
            result["browser_started"] = True
            page = context.pages[0] if context.pages else context.new_page()
            page.goto(URL, wait_until="domcontentloaded", timeout=45000)
            result["facebook_loaded"] = "facebook.com" in page.url
            # A heuristic, NOT proof of successful authentication.
            result["login_status"] = ("login_or_challenge" if
                any(word in page.url.lower() for word in ("login", "checkpoint", "recover")) else
                "unverified_session")
            context.close()
    except Exception as exc:
        result["error"] = str(exc)[:400]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    run()
