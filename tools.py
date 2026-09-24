"""
tools.py
Simple web-search helper for Current Affairs style topics, using
duckduckgo-search (no API key needed).
"""

from duckduckgo_search import DDGS


def web_search(query: str, max_results: int = 5):
    """Returns a list of dicts: {title, href, body}."""
    try:
        with DDGS() as ddgs:
            return list(ddgs.text(query, max_results=max_results))
    except Exception:
        return []


def format_search_results(results) -> str:
    if not results:
        return "No search results found."
    lines = []
    for r in results:
        title = r.get("title", "")
        body = r.get("body", "")
        href = r.get("href", "")
        lines.append(f"- {title}: {body} ({href})")
    return "\n".join(lines)
