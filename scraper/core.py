from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Iterable

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com/page/{page}/"
USER_AGENT = "WebScraperToolkit/1.0 (+https://github.com/lumufa/web-scraper-toolkit)"
REQUEST_TIMEOUT = 15


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str] = field(default_factory=list)


def fetch_page(page: int, session: requests.Session) -> str:
    response = session.get(BASE_URL.format(page=page), timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.text


def parse_page(html: str) -> list[Quote]:
    soup = BeautifulSoup(html, "lxml")
    quotes: list[Quote] = []
    for card in soup.select("div.quote"):
        text_el = card.select_one("span.text")
        author_el = card.select_one("small.author")
        if not text_el or not author_el:
            continue
        tags = [t.get_text(strip=True) for t in card.select("div.tags a.tag")]
        quotes.append(
            Quote(
                text=text_el.get_text(strip=True).strip("“”"),
                author=author_el.get_text(strip=True),
                tags=tags,
            )
        )
    return quotes


def scrape_pages(pages: Iterable[int], delay: float = 1.0) -> list[Quote]:
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    results: list[Quote] = []
    for i, page in enumerate(pages):
        if i > 0:
            time.sleep(delay)
        html = fetch_page(page, session)
        page_quotes = parse_page(html)
        if not page_quotes:
            break
        results.extend(page_quotes)
    return results
