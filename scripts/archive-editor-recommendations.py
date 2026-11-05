#!/usr/bin/env python3
"""Archive the public CKEditor recommendations site; no third-party scripts run.

Raw responses and readable text are local research, not Apache-2.0 project source.
The default destination is ignored by Git. A manifest records coverage and hashes.
"""
import argparse
import hashlib
import json
import re
import time
from collections import deque
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlsplit, unquote
from urllib.request import Request, urlopen

BASE = 'https://ckeditor.github.io/editor-recommendations/'
LICENSE = 'https://creativecommons.org/licenses/by-nc-sa/4.0/'


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.assets, self.text = [], [], []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in ('img', 'script', 'source') and attrs.get('src'):
            self.assets.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') in ('stylesheet', 'icon', 'shortcut icon'):
            self.assets.append(attrs.get('href', ''))
        if tag in ('p', 'div', 'li', 'br', 'tr', 'h1', 'h2', 'h3', 'h4', 'pre'):
            self.text.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        if tag in ('p', 'div', 'li', 'tr', 'h1', 'h2', 'h3', 'h4', 'pre'):
            self.text.append('\n')

    def handle_data(self, value):
        if not self.hidden:
            self.text.append(value)


def canonical(url):
    url = urldefrag(url)[0]
    p = urlsplit(url)
    if p.hostname != 'ckeditor.github.io' or not p.path.startswith('/editor-recommendations/'):
        return None
    if p.query or '..' in unquote(p.path).split('/'):
        return None
    return 'https://ckeditor.github.io' + p.path


def archive(destination):
    destination.mkdir(parents=True, exist_ok=False)
    pending = deque([BASE])
    visited, external, records, failures = set(), set(), [], []
    while pending:
        url = pending.popleft()
        if url in visited:
            continue
        visited.add(url)
        try:
            with urlopen(Request(url, headers={'User-Agent': 'edit.ac-local-reference-archive/1.0'}), timeout=30) as response:
                final = canonical(response.url)
                if not final:
                    raise ValueError('Redirect left the requested site')
                body = response.read(16 * 1024 * 1024 + 1)
                if len(body) > 16 * 1024 * 1024:
                    raise ValueError('Resource exceeds 16 MiB bound')
                mime = response.headers.get_content_type()
            if final in visited and final != url:
                continue
            visited.add(final)
            relative = unquote(urlsplit(final).path[len('/editor-recommendations/'):])
            if not relative or relative.endswith('/'):
                relative += 'index.html'
            path = destination / 'raw' / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
            row = dict(url=url, final_url=final, path=str(path.relative_to(destination)),
                       content_type=mime, bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
            refs = []
            if mime == 'text/html':
                page = Page()
                page.feed(body.decode('utf-8'))
                readable = '\n'.join(line.strip() for line in ''.join(page.text).splitlines() if line.strip())
                text_path = destination / 'text' / (relative + '.txt')
                text_path.parent.mkdir(parents=True, exist_ok=True)
                text_path.write_text(f'Source: {final}\nCopyright CKSource; CC BY-NC-SA 4.0\nLicense: {LICENSE}\n\n{readable}\n')
                row['text_path'] = str(text_path.relative_to(destination))
                refs = page.links + page.assets
            elif mime == 'text/css':
                refs = re.findall(r'url\([\s\"\']*([^\)\"\']+)', body.decode('utf-8'))
            for ref in refs:
                resolved = urljoin(final, ref)
                scoped = canonical(resolved)
                if scoped:
                    if scoped not in visited:
                        pending.append(scoped)
                elif resolved.startswith(('http:', 'https:')):
                    external.add(resolved)
            records.append(row)
        except Exception as error:
            failures.append(dict(url=url, error=str(error)))
        time.sleep(0.1)
    manifest = dict(base_url=BASE, fetched_at=datetime.now(timezone.utc).isoformat(),
                    scope='All reachable same-site pages and referenced same-site assets; external sites excluded',
                    license=LICENSE, records=records, failures=failures,
                    external_links=sorted(external))
    (destination / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    pages = [r for r in records if 'text_path' in r]
    (destination / 'README.md').write_text(
        '# CKEditor Editor Recommendations — local reference archive\n\n'
        f'Source: {BASE}\n\nCopyright © 2015–2019 CKSource Frederico Knabben. '
        f'License: [CC BY-NC-SA 4.0]({LICENSE}). Retain attribution and source license.\n\n'
        'Raw bytes are unchanged. Text files remove scripts/styles and collapse layout whitespace; '
        'they retain document text, navigation and notices. Read these without a network connection. '
        'Raw HTML is evidence, not a runnable offline application. External CDN assets and analytics are excluded.\n\n'
        + '\n'.join(f'- [{r["final_url"]}]({r["text_path"]})' for r in pages) + '\n')
    print(json.dumps(dict(destination=str(destination), pages=len(pages), resources=len(records), failures=failures)))
    return bool(failures)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, default=Path(__file__).resolve().parents[1] / '.artifacts' / 'editing-reference' / 'ckeditor-20261024')
    raise SystemExit(archive(parser.parse_args().destination))
