package utils

import (
	"strings"

	"github.com/PuerkitoBio/goquery"
	"github.com/go-resty/resty/v2"
)

var restyClient = resty.New()

func GetPageContent(username, password, url string) string {
	initialResponse, _ := restyClient.R().
			EnableTrace().
			Get("https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f")

	doc, _ := goquery.NewDocumentFromReader(strings.NewReader(initialResponse.String()))

	requestVerificationToken, _ := doc.Find("[name='__RequestVerificationToken']").Attr("value")
	cookies := initialResponse.Cookies()

	requestHeaders := map[string]string{
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
		"X-Requested-With": "XMLHttpRequest",
		"Host": "hac.friscoisd.org",
		"Origin": "hac.friscoisd.org",
		"Referer": "https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fhomeaccess%2f",
		"__RequestVerificationToken": requestVerificationToken,
	}

	requestPayload := map[string]string{
		"__RequestVerificationToken" : requestVerificationToken,
		"SCKTY00328510CustomEnabled" : "False",
		"SCKTY00436568CustomEnabled" : "False",
		"Database" : "10",
		"VerificationOption" : "UsernamePassword",
		"LogOnDetails.UserName": username,
		"tempUN" : "",
		"tempPW" : "",
		"LogOnDetails.Password" : password,
	}

	restyClient.SetCookies(cookies)
	restyClient.SetHeaders(requestHeaders)
	restyClient.SetFormData(requestPayload)

	homepageResponse, _ := restyClient.R().
		EnableTrace().
		Post("https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f")
	
	cookies = homepageResponse.Cookies()
	restyClient.SetCookies(cookies)
	
	finalResponse, _ := restyClient.R().
		EnableTrace().Get(url)
	
	return finalResponse.String()
}