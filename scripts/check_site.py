#!/usr/bin/env python3
"""Check the static site: local links, fragments, counts, and retired claims.

Usage: python3 scripts/check_site.py
Uses only the standard library. It reads files; it does not serve or build anything.
A passing run proves link structure, not content accuracy or accessibility.
"""
from collections import Counter
from html.parser import HTMLParser
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CDN_HOSTS = ("cdn.jsdelivr.net", "cdnjs.cloudflare.com")
RETIRED = (
    "production-grade security framework",
    "tamper-proof audit trail",
    "FIPS 140-2 encryption",
    "expected early 2027",
    "8 services",
    "preventing hallucination by design",
)


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        for name in ("href", "src"):
            value = attributes.get(name)
            if value:
                self.links.append(value)


def pages():
    return sorted(p for p in ROOT.rglob("*.html") if ".git" not in p.parts)


def main():
    documents = pages()
    failures = []
    parsed = {}
    for page in documents:
        collector = Collector()
        collector.feed(page.read_text())
        parsed[page] = collector
        duplicates = [i for i, n in Counter(
            tag_id for tag_id in collector.ids).items() if n > 1]
        if duplicates:
            failures.append(f"{page.relative_to(ROOT)}: duplicate ids {duplicates}")

    for page, collector in parsed.items():
        if "template" in page.name:
            continue  # Authoring templates carry documented placeholders, not real links.
        for link in collector.links:
            if link.startswith(("http://", "https://", "mailto:", "#", "data:")):
                if link.startswith("https://") and not any(
                        host in link for host in CDN_HOSTS) and link.endswith(".css"):
                    failures.append(f"{page.relative_to(ROOT)}: unexpected remote stylesheet {link}")
                if link.startswith("#") and link[1:] and link[1:] not in collector.ids:
                    failures.append(f"{page.relative_to(ROOT)}: missing fragment {link}")
                continue
            target, _, fragment = link.partition("#")
            resolved = (page.parent / target).resolve()
            if not resolved.exists():
                failures.append(f"{page.relative_to(ROOT)}: broken local target {link}")
                continue
            if fragment and resolved.suffix == ".html":
                if fragment not in parsed.get(resolved, Collector()).ids and resolved.exists():
                    other = Collector()
                    other.feed(resolved.read_text())
                    if fragment not in other.ids:
                        failures.append(
                            f"{page.relative_to(ROOT)}: missing fragment {link}")

    for page in documents:
        text = page.read_text()
        for phrase in RETIRED:
            if phrase in text:
                failures.append(f"{page.relative_to(ROOT)}: retired claim {phrase!r}")

    reader_pages = [p for p in documents if "template" not in p.name]
    print(f"HTML files: {len(documents)} ({len(reader_pages)} reader pages, "
          f"{len(documents) - len(reader_pages)} templates)")
    for failure in failures:
        print("FAIL", failure, file=sys.stderr)
    if failures:
        return 1
    print("Local links, fragments, ids, and retired claims: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
