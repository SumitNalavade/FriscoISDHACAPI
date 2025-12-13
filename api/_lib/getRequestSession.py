import requests
from bs4 import BeautifulSoup

LOGIN_URL = "https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f"

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/36.0.1985.125 Safari/537.36"
)

def _extract_verification_token(html: str) -> str:
    """Parse the login page and return __RequestVerificationToken or raise."""
    soup = BeautifulSoup(html, "lxml")
    token_input = soup.find("input", attrs={"name": "__RequestVerificationToken"})
    if not token_input or "value" not in token_input.attrs:
        raise RuntimeError("Unable to find __RequestVerificationToken on login page.")
    return token_input["value"]


def getRequestSession(username: str, password: str) -> requests.Session:
    session = requests.Session()

    session.headers.update({"User-Agent": DEFAULT_USER_AGENT})

    resp = session.get(LOGIN_URL)
    resp.raise_for_status()
    request_verification_token = _extract_verification_token(resp.text)

    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Referer": LOGIN_URL,
        "__RequestVerificationToken": request_verification_token,
    }

    payload = {
        "__RequestVerificationToken": request_verification_token,
        "SCKTY00328510CustomEnabled": "False",
        "SCKTY00436568CustomEnabled": "False",
        "Database": "10",
        "VerificationOption": "UsernamePassword",
        "LogOnDetails.UserName": username,
        "tempUN": "",
        "tempPW": "",
        "LogOnDetails.Password": password,
    }

    login_resp = session.post(LOGIN_URL, data=payload, headers=headers)
    login_resp.raise_for_status()

    return session
