from bs4 import BeautifulSoup

def _get_text_or_empty_by_id(soup: BeautifulSoup, element_id: str) -> str:
    el = soup.find(id=element_id)
    return el.get_text(strip=True) if el else ""

def _get_texts_by_css_selector(soup: BeautifulSoup, selector: str) -> list[str]:
    return [el.get_text(strip=True) for el in soup.select(selector)]

def _get_first_text_or_empty_by_css_selector(soup: BeautifulSoup, selector: str) -> str:
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else ""