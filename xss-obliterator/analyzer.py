SOURCES = [
    "location",
    "window.location",
    "document.location",
    "document.URL",
    "URLSearchParams",
    "location.search",
    "location.hash"
]


SINKS = [
    "innerHTML",
    "outerHTML",
    "innerText",
    "document.write",
    "eval(",
    "setTimeout(",
    "setInterval(",
    "insertAdjacentHTML",
    "location.href",
    ".src =",
    ".href ="
]


def analyze(js_code):
    findings = []
    for src in SOURCES:
        if src in js_code:
            for sink in SINKS:
                if sink in js_code:
                    findings.append((src, sink))
    return findings
