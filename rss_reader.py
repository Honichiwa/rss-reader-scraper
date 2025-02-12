from argparse import ArgumentParser
from typing import List, Optional, Sequence
import xml.etree.ElementTree as ET
import requests
import json as _json

class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json_output: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    result_list = []
    root = ET.fromstring(xml)
    channel = root.find("channel")

    feed_title = channel.findtext("title")
    result_list.append(f"Feed: {channel.findtext('title')}\n")

    link = channel.findtext("link")
    result_list.append(f"Link: {channel.findtext('link')}\n")

    last_build_date = channel.findtext('lastBuildDate')
    result_list.append(f"Last build date: {channel.findtext('lastBuildDate')}\n")

    pub_date = channel.findtext('pubDate')
    result_list.append(f"Published: {channel.findtext('lastBuildDate')}\n")

    language = channel.findtext('language')
    result_list.append(f"Language: {channel.findtext('language')}\n")

    category = [category for category in channel.findall("category")]
    result_list.append(f"Category: {channel.findtext('category')}\n")

    managing_editor = channel.findtext('managingEditor')
    result_list.append(f"Managing Editor: {channel.findtext('managingEditor')}\n")

    description = channel.findtext("description")
    result_list.append(f"Description: {channel.findtext('description')}\n")


    items = [item for item in channel.findall("item")]
    if limit:
        items = items[:limit]

    item_list = []
    for item in items:
        item_list.append(f"\nTitle: {item.findtext('title')}\n")
        item_list.append(f"Author: {item.findtext('author')}\n"),
        item_list.append(f"Published: {item.findtext('pubDate')}\n")
        item_list.append(f"Link: {item.findtext('link')}\n")
        item_list.append(f"Category: {item.findtext('category')}\n")
        item_list.append(f"\n{item.findtext('description')}")
        item_list.append(f"\n")


    if json:
        result = {
            "title": feed_title,
            "link": link,
            "lastBuildDate": last_build_date,
            "pubDate": pub_date,
            "language": language,
            "category": category,
            "managingEditor": managing_editor,
            "description": description,
            "items": [{
                "title": item.findtext("title"),
                "author": item.findtext("author"),
                "pubDate": item.findtext("pubDate"),
                "link": item.findtext("link"),
                "category": item.findtext("category"),
                "description": item.findtext("description"),

                       }

                for item in items
                ],
        }
        return [_json.dumps(result, indent=2)]

    return result_list + item_list

def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)

    if args.source is None:
        parser.print_help()
        exit(1)
    
    xml = requests.get(args.source).text
    try:
        print("".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
