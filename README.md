# Web Scraper Toolkit

A clean, configurable web scraper built with Python `requests` and `BeautifulSoup`. Designed as a starting point for custom scraping projects: pagination, polite rate limiting, and CSV/JSON output out of the box.

This repository scrapes [quotes.toscrape.com](https://quotes.toscrape.com) — a public site explicitly designed for scraping practice — but the same structure applies to any static HTML target.

## Features

- Pagination handling (scrape any page range)
- Polite rate limiting between requests
- Pluggable exporters: CSV and JSON
- Clean separation of fetching, parsing, and exporting logic
- Type hints throughout
- Zero hard-coded selectors in the CLI — easy to retarget

## Requirements

- Python 3.10+
- See `requirements.txt`

## Install

```bash
git clone https://github.com/lumufa/web-scraper-toolkit.git
cd web-scraper-toolkit
pip install -r requirements.txt
```

## Usage

Scrape the first 3 pages of quotes and save as CSV:

```bash
python main.py --pages 1-3 --format csv --output quotes.csv
```

Scrape pages 1 to 10 as JSON:

```bash
python main.py --pages 1-10 --format json --output quotes.json
```

### CLI Options

| Flag | Description | Default |
|------|-------------|---------|
| `--pages` | Page range, e.g. `1-5` or `3` | `1-1` |
| `--format` | Output format: `csv` or `json` | `csv` |
| `--output` | Output file path | `quotes.csv` |
| `--delay` | Seconds between requests | `1.0` |

## Sample Output

CSV:

```csv
text,author,tags
"The world as we have created it...","Albert Einstein","change;deep-thoughts;thinking;world"
```

See `examples/` for full sample outputs.

## Project Structure

```
web-scraper-toolkit/
├── main.py              # CLI entry point
├── scraper/
│   ├── __init__.py
│   ├── core.py          # Fetch + parse logic
│   └── exporters.py     # CSV / JSON exporters
├── examples/            # Sample outputs
├── requirements.txt
└── README.md
```

## Retargeting to Another Site

To scrape a different site, edit `scraper/core.py`:

1. Update `BASE_URL` and `parse_page()` selectors
2. Adjust the dataclass `Quote` to match the data you're extracting
3. Update exporters if the schema changes

## License

MIT
