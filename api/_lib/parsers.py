from bs4 import BeautifulSoup

def _get_text_or_empty_by_id(soup: BeautifulSoup, element_id: str) -> str:
    """Return the stripped text of an element by id, or empty string if missing."""
    el = soup.find(id=element_id)
    return el.get_text(strip=True) if el else ""

def _get_text_or_empty_by_css_selector(soup: BeautifulSoup, selector: str) -> str:
    el = soup.select(selector)
    return [elm.get_text(strip=True) if elm else "" for elm in el]