import requests
from bs4 import BeautifulSoup
import lxml

def getRequestSession(username, password):
    requestSession = requests.session()

    loginScreenResponse = requestSession.get("https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f").text

    parser =  BeautifulSoup(loginScreenResponse, "lxml")

    requestVerificationToken = parser.find('input', attrs={'name': '__RequestVerificationToken'})["value"]

    requestHeaders = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Host': 'hac.friscoisd.org',
        'Origin': 'hac.friscoisd.org',
        'Referer': "https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fhomeaccess%2f",
        '__RequestVerificationToken': requestVerificationToken
    }

    requestPayload = {
        "__RequestVerificationToken" : requestVerificationToken,
        "SCKTY00328510CustomEnabled" : "False",
        "SCKTY00436568CustomEnabled" : "False",
        "Database" : "10",
        "VerificationOption" : "UsernamePassword",
        "LogOnDetails.UserName": username,
        "tempUN" : "",
        "tempPW" : "",
        "LogOnDetails.Password" : password
    }

    pageDOM = requestSession.post(
        "https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f",
        data=requestPayload,
        headers=requestHeaders
    )

    return requestSession

