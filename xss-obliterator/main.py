# main.py
import argparse
from banner import show_banner
from js_fetcher import fetch_js
from analyzer import analyze
from verifier import verify_dom_xss

HELP_EPILOG = """
Tags explained:
  [DOM-XSS]        Potential DOM-based XSS source → sink flow
  [🔥] EXPLOITABLE  XSS payload executed successfully
  [✓] SAFE         No exploitable XSS found
  [i] INFO         Informational message
  [!] WARNING      Partial failure (timeouts, blocked fetches)

Examples:
  python main.py -u https://example.com
  python main.py -u http://localhost:3000/#/search --verify
"""

def main():
    show_banner()

    parser = argparse.ArgumentParser(
        description="xss-obliterator — DOM XSS recon + exploit verification",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=HELP_EPILOG
    )

    parser.add_argument(
        "-u", "--url",
        required=True,
        help="Target URL to scan"
    )

    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify exploitability using a real browser"
    )

    args = parser.parse_args()

    print(f"[+] Scanning {args.url}")

    scripts = fetch_js(args.url)
    print(f"[+] JavaScript blocks found: {len(scripts)}")

    if not scripts:
        print("[✓] SAFE — no JavaScript to analyze.")
        return

    findings = set()

    for js in scripts:
        results = analyze(js)
        for src, sink in results:
            findings.add((src, sink))

    if not findings:
        print("[✓] SAFE — no DOM XSS vulnerabilities found.")
        return

    print("\n[!] Potential DOM XSS patterns detected:")
    for src, sink in findings:
        print(f"    [DOM-XSS] {src} → {sink}")

    if args.verify:
        print("\n[*] Verifying exploitability in real browser...")
        exploitable = verify_dom_xss(args.url)

        if exploitable:
            print("[🔥] EXPLOITABLE — DOM XSS confirmed")
        else:
            print("[✓] SAFE — not exploitable under tested conditions")
    else:
        print("\n[i] INFO — use --verify to confirm exploitability")

    print("\n[✓] Scan completed.")

if __name__ == "__main__":
    main()
