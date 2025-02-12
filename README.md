# RSS Reader & Scraper

A simple command-line RSS reader and scraper written in Python. This tool fetches and parses RSS feeds, allowing users to view news articles in plain text or JSON format.

## Features
- Fetches and parses RSS feeds
- Outputs data in plain text or JSON format
- Limits the number of articles displayed
- Handles XML parsing errors gracefully

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Honichiwa/rss-reader-scraper.git
   cd rss-reader-scraper
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

Run the script with an RSS feed URL:
```sh
python rss_parser.py <RSS_FEED_URL>
```

### Options:
- `--json` : Output the feed data in JSON format.
- `--limit <number>` : Limit the number of articles displayed.
- `-h` : Show help message.

#### Example Usage:
```sh
python rss_parser.py https://www.yahoo.com/news/rss --json --limit 5
```

## Requirements
- Python 3.7+
- Requests
- Argparse

## Error Handling
If no arguments are provided, the script will display the help message.
