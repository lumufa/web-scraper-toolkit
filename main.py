from __future__ import annotations

import argparse
import sys

from scraper import export_csv, export_json, scrape_pages


def parse_page_range(value: str) -> range:
    if "-" in value:
        start_str, end_str = value.split("-", 1)
        start, end = int(start_str), int(end_str)
    else:
        start = end = int(value)
    if start < 1 or end < start:
        raise argparse.ArgumentTypeError(f"Invalid page range: {value}")
    return range(start, end + 1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scrape quotes from quotes.toscrape.com and export as CSV or JSON."
    )
    parser.add_argument(
        "--pages",
        type=parse_page_range,
        default=parse_page_range("1-1"),
        help="Page range, e.g. '1-5' or '3'. Default: 1-1.",
    )
    parser.add_argument(
        "--format",
        choices=["csv", "json"],
        default="csv",
        help="Output format. Default: csv.",
    )
    parser.add_argument(
        "--output",
        default="quotes.csv",
        help="Output file path. Default: quotes.csv.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Seconds between requests. Default: 1.0.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    print(f"Scraping pages {args.pages.start}-{args.pages.stop - 1}...")
    quotes = scrape_pages(args.pages, delay=args.delay)
    print(f"Collected {len(quotes)} quotes.")

    if args.format == "csv":
        export_csv(quotes, args.output)
    else:
        export_json(quotes, args.output)

    print(f"Saved to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
