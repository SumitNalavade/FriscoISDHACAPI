import requests
from bs4 import BeautifulSoup
from AppError import AppError

LOGIN_URL = "https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f"
TRANSCRIPT_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Transcript.aspx"
REGISTRATION_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Registration.aspx"
CLASSES_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"
SATSCHEDULE_URL = "https://satsuite.collegeboard.org/sat/registration/dates-deadlines"
STUDENTSCHEDULE_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Classes.aspx"

doubleWeighted = ['gt', 'physics c', 'veterinary', 'equipment', 'architectural design 2', 'interior design 2', 'animation', 'sports broadcasting', 'graphic Design', 'child guidance',
'education and training', 'practicum in govern', 'clinical', 'electrocardiography', 'medical technician', 'hospitality', 'culinary', 'ap computer', 'sports management']

# Create a BS4 object to parse the HTML string
def createBS4Parser(content):
    return BeautifulSoup(content, "html.parser")

#Extract the requestVerificationToken needed in the headers
#Return a tuple containing the token and the request session
#Note: The requestVerificationToken is linked to the request session so any function using the token must also use the request session
def getRequestVerificationToken():
    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)
    parser = createBS4Parser(result.text)
    return [parser.find('input', attrs={'name': '__RequestVerificationToken'})["value"], session_requests]
    

def createRequestHeaders(requestVerificationToken):
    return {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'hac.friscoisd.org',
    'Origin': 'hac.friscoisd.org',
    'Referer': "https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fhomeaccess%2f",
    '__RequestVerificationToken': requestVerificationToken
    }

def createRequestPayload(username, password, requestVerificationToken):
    return {
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

def createPastAssignmentRequestHeader():
    return {
        "Host": "hac.friscoisd.org",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
        'X-Requested-With': 'XMLHttpRequest',
        "Origin": "https://hac.friscoisd.org",
        "Referer": "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx",
    }

def createPastAssignmentRequestPayload(quarter):
    wanted = f"{quarter}-2022"
    return {
	"__EVENTTARGET": "ctl00$plnMain$btnRefreshView",
	"__EVENTARGUMENT": "",
	"__VIEWSTATE": "EUztZv6fUH/kfpDA/0Vv7SjKlDuvPaiQLQojMxnFqbw4cOJAMgOvezlnjYoVywYQJHMRgkCC3K2Le7tjDvmZd1u8bdH3a3rzCOE+KiiNqTh5adwLxFahHC1Q+Z0PBi9S0HH+LEHtn6yF7yCACpwdbjU0dnnIi+cILRKjGt/5c30lZgSMEUE+Kqne+GrJoqvtN2qwS7TrYzLBZw9RKIyoZxb0qs8kZ65JuROtgOKiU/3eveBA5Pyx/lOyTuXEk9i0ztJeW7pyCrPWXtfJOKfgyczTkmFFd4QSAdXOCjAkwlEMr0erVIf9HSr30DbBTs2LP5GBCCFRZd1WPXpHExjrp3GLVJdKBT8zaZvIo1LZzuQI6PSPEwc/u4VNxZSbiwRR1aJYcaLto5Wy0UD0xS+ZgCKYhRhcQFwrVRdquwikEqORbL+OCpjSgXziFQOVOh+HfwGjpMBAfGQTp3Zip7f53Lt5wdgenrLJscMhAMIxESyonfJVDzLBhXH2Cgqh80KoSs696UymJsFvwoPOCzoBfGIOp4NijZsqr6PRBsIRas9O4NYbl/QLWhF1q/tdiFKUUWYRUm6Bb2kSu9+w2pdOJYVxGhQv0jKCuu6uC2zQ1bixIzMtQXFyd0MNpmQ5MZhVPlR0I9yFS6aLaUAZL5ej/5DTCpfqPV0uDGP2+3Qd9Ugr5u4p8/ey+2eyB5NT4zKF4ELNLskXNkB/BM2z5uNZCpN1owWbjJOkVrfR6NYch+tD+TpYPBg2/xDG9ubrHngoE/n7+q/jaIcjy7psUiPwRq+sUjh7AwlBHv38mfGArMV+89MgzzioI0AD5vHrru36avcsQ9wtl4kXKh3mIqSfU46q99toJ1Wd43bJSXoYbfkjYqNserO+CU0Om9qpRh/OG32VOBs7ZiwrRmIBzpe5vw1Krb7QaLyP9ye9UPyueT4Qo0QCuVaQvibmuQ5zzhsRnQyA0CUFaTccmsu0s8S9O6ek6ldtsaC6i9c40XuBBvCRoq6XbgWz1RgqIwKcUVThTxJZ6LlUJVhb5VBXlJYfxY0OSPlvW/b8XqEuzaFQyYZ0/RSczqnral0gbX3EatD+L5htFc72y3/9YO+Edbbl/K/7/n3Ei3QHp7vcnTqbbKKu1O0m6Q5izgGARDFdpFDtrMk/0QiHGtvli4dmPqgcX+P2qPHpnxFGPj9SGXfhVbfoCKatMe5Nx/78+YwVGehysdzRPXmdxtivlSitUsEdMZXxhD4+PeM1zmaQ4CkCvy5Pr8s1LrlsvVzjF/cSJu5Xwgwpdd0acZNwzIQdzonEQgS6zlBe8eDtWubrH5cnR33yRrs0evnApS9yUPsPgn36LGF15zYqVAYNUcUG5rfQcDw1Bpui9j7o4Xx4LOymyZemZKjPX1K7NGvgWi18710IDnzPyB5X0Kh9gf+xXio7StRZiL90mkbMoTfE6z12Rhg9FVNxoZKfX292d2nNNs7ExNDbOpM24pnVVtlW4ueAdPejZcNoC0Gre3v4LCZERMSYKnsV6Q1X/DVjb8yTwuBs44GImsDOuscvxXI0HdfcXKgKLjbMJqnF8P0GXzzNMTUHRhzFQO9wddLD0+U9LSIPRBE/F/4Nn8F9QOerpMCaYsS9L6Oxo0gXxOL8dDeaD2A=",
	"__VIEWSTATEGENERATOR": "B0093F3C",
	"__EVENTVALIDATION": "rVo6Q349ar26gUtGfuaIiHzqYF9IMaPUlIEkCa5nKFTVNfEeYkNuktWuIsqYFhLBJ4AVziUTJbNmofQQ9tPbuGifh+uXywyqHS9+cJ+3E1ezGsGYgwXkYNgFXiYl+yhrYa0JcMMxamGAqqKiZ/ohNwmPd9oYaJ12Fr2+WpxeomrYGWelYDARX5azu0dPUeYVpjg/mdYi5iq97fz317B1vJitegkiLAOt8P1uf59dmKrY0Dxjjt4uvlgZsWdRM47C5wgFnMYpdWercGXdAMGFTcBSPdJxPElzB5LOB52LT6iZCJVv4HFZeIXcgtEaeO3YBJ/1GMcoSVgvL4d1/nK/71dncky39p9MxBiJUHVsIip3FPceiKYuOJY+r6N60Gh31bUbg/YuC9sYAuQjtxjZE2mVI6Hwb7879Gt95KOphNHeHQcctqivfO/a52MJRVzbonj/4EfoGuyeyiw1eshlum9/xa9/lbe2cAjG02Ht26y3LfdF5MmLyP18B9PSWGP6zcJNxrMEWS/nXwIHUKU0FahZHP8l1oq7Q+nPbXrowWNZc5kmkRPCr+EG6IkHzK/c6xmSw9Az29Ho87//IogXdNUQTMjtGGLD5z+ImVaL2RI5bHnRv8DYxDcsMOCWbL0EEuarDThYrXpci1ihkEV3fBi3c2zfRF0ONBPWSrgpwBGn/GAUomy19O6BdGg0otFFZyo+9aAhRrK/zCnF/J1JbKQuc33Teajh7CaW9hkbOXMCr+71Mreb0VD2uKhA/UQWuPR7MKKUsQ3jtwY7VURKbD0V2mq3NTIBNuI6Gtp1Jiw6Wqi8L8S9tPo7ToK9+IEi4ZatkJOMDxQOIMXoRKRvjm7at0eMc9RRzMvAQ8lrLaLjUcDNSEAfkGJjbB+o7ztTzTUUQyt2VG6ZaMkQvAEDjq8pB7Q239rrpD2f5OHtksvdtnFjUqRDGMqgE8ANep/Ubl0Kq3Pf8vrzGA4V6xAsxvkgy1xhQ7YMHJeWl1VX6LYs6sEVbTM07nt45b/HSUbTSeuBKFnF0HgzZcYKd3xdS3eKchlqiu1nmGgbgXP8QRvfl+TBR2Qn90RUQxvHdWcECXS0Fy4JN0D9Drh8SeNvgS6PUncY4GySrIQ92lvkkm3T6xptXdRhcyuoxOvpcLLcNaim3LS4Odh6QrNd1nN5+7fV6bKSSK/gGrz8AvWBQM+Vhr1Ls15gX3l9cUcNif3uqbmY0JNHdbm0DlNl8K60go+tTXpRDK/w8YYMoNt1e7lWHCI5UuDf9dRTk2yahgtf4p+Gbpk/zxaxaihxrCPv7jX57zquSRw3hhI3qDMvCi+uAdglLvFYv4+CsR08oDLgNHOnUGAR7optvJiv2mnbGnacnJ8v9t0Bw1Hlzf6bLJWPi+44BkDNvxTgDSgmLYAU9xWtgvKMdBfkt3m1V0pfcpJFe8u9ka2c8Hkc8W0XU2gNjVzMn6PMfkswaLIr+OUMHt440s1EP3AB0N6GL1IGyPqhkzYtWcTJBEiKD01ptMdQb8XGPTCsIwL80n8UzWStQzNl9NZ2ukk2sxKkXym6Xv/kYEsLuSrwgLu6/Mpa502YOa654JHYidiSaV2ES58l",
	"ctl00$plnMain$hdnValidMHACLicense": "Y",
	"ctl00$plnMain$hdnIsVisibleClsWrk": "N",
	"ctl00$plnMain$hdnIsVisibleCrsAvg": "N",
	"ctl00$plnMain$hdnJsAlert": "Averages+cannot+be+displayed+when++Report+Card+Run+is+set+to+(All+Runs).",
	"ctl00$plnMain$hdnTitle": "Classwork",
	"ctl00$plnMain$hdnLastUpdated": "Last+Updated",
	"ctl00$plnMain$hdnDroppedCourse": "+This+course+was+dropped+as+of+",
	"ctl00$plnMain$hdnddlClasses": "(All+Classes)",
	"ctl00$plnMain$hdnddlCompetencies": "(All+Classes)",
	"ctl00$plnMain$hdnCompDateDue": "Date+Due",
	"ctl00$plnMain$hdnCompDateAssigned": "Date+Assigned",
	"ctl00$plnMain$hdnCompCourse": "Course",
	"ctl00$plnMain$hdnCompAssignment": "Assignment",
	"ctl00$plnMain$hdnCompAssignmentLabel": "Assignments+Not+Related+to+Any+Competency",
	"ctl00$plnMain$hdnCompNoAssignments": "No+assignments+found",
	"ctl00$plnMain$hdnCompNoClasswork": "Classwork+could+not+be+found+for+this+competency+for+the+selected+report+card+run.",
	"ctl00$plnMain$hdnCompScore": "Score",
	"ctl00$plnMain$hdnCompPoints": "Points",
	"ctl00$plnMain$hdnddlReportCardRuns1": "(All+Runs)",
	"ctl00$plnMain$hdnddlReportCardRuns2": "(All+Terms)",
	"ctl00$plnMain$hdnbtnShowAverage": "Show+All+Averages",
	"ctl00$plnMain$hdnShowAveragesToolTip": "Show+all+student's+averages",
	"ctl00$plnMain$hdnPrintClassworkToolTip": "Print+all+classwork",
	"ctl00$plnMain$hdnPrintClasswork": "Print+Classwork",
	"ctl00$plnMain$hdnCollapseToolTip": "Collapse+all+courses",
	"ctl00$plnMain$hdnCollapse": "Collapse+All",
	"ctl00$plnMain$hdnFullToolTip": "Switch+courses+to+Full+View",
	"ctl00$plnMain$hdnViewFull": "Full+View",
	"ctl00$plnMain$hdnQuickToolTip": "Switch+courses+to+Quick+View",
	"ctl00$plnMain$hdnViewQuick": "Quick+View",
	"ctl00$plnMain$hdnExpand": "Expand+All",
	"ctl00$plnMain$hdnExpandToolTip": "Expand+all+courses",
	"ctl00$plnMain$hdnChildCompetencyMessage": "This+competency+is+calculated+as+an+average+of+the+following+competencies",
	"ctl00$plnMain$hdnCompetencyScoreLabel": "Grade",
	"ctl00$plnMain$hdnAverageDetailsDialogTitle": "Average+Details",
	"ctl00$plnMain$hdnAssignmentCompetency": "Assignment+Competency",
	"ctl00$plnMain$hdnAssignmentCourse": "Assignment+Course",
	"ctl00$plnMain$hdnTooltipTitle": "Title",
	"ctl00$plnMain$hdnCategory": "Category",
	"ctl00$plnMain$hdnDueDate": "Due+Date",
	"ctl00$plnMain$hdnMaxPoints": "Max+Points",
	"ctl00$plnMain$hdnCanBeDropped": "Can+Be+Dropped",
	"ctl00$plnMain$hdnHasAttachments": "Has+Attachments",
	"ctl00$plnMain$hdnExtraCredit": "Extra+Credit",
	"ctl00$plnMain$hdnType": "Type",
	"ctl00$plnMain$hdnAssignmentDataInfo": "Information+could+not+be+found+for+the+assignment",
	"ctl00$plnMain$ddlReportCardRuns": wanted,
	"ctl00$plnMain$ddlClasses": "ALL",
	"ctl00$plnMain$ddlCompetencies": "ALL",
	"ctl00$plnMain$ddlOrderBy": "Class"
    }


#Return the page of the final location
def getPage(username, password, pageURL):
    try:
        (requestVerificationToken, session_requests) = getRequestVerificationToken()
    except:
        return AppError(500, "HAC Server Error")

    requestHeaders = createRequestHeaders(requestVerificationToken)
    requestPayload = createRequestPayload(username, password, requestVerificationToken)

    #Get through the login screen
    pageDOM = session_requests.post(
        LOGIN_URL,
        data=requestPayload,
        headers=requestHeaders
    )

    #Throw a 500 error if the login fails
    if(pageDOM.url == "https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2FHomeAccess%2F"):
        return AppError(400, "HAC login failed")

    #Reroute to the final page
    pageDOM = session_requests.get(pageURL)

    return pageDOM

def getPastAssignments(username, password, quarter):
    try:
        (requestVerificationToken, session_requests) = getRequestVerificationToken()
    except:
        return AppError(500, "HAC Server Error")

    requestHeaders = createRequestHeaders(requestVerificationToken)
    requestPayload = createRequestPayload(username, password, requestVerificationToken)

    #Get through the login screen
    pageDOM = session_requests.post(
        LOGIN_URL,
        data=requestPayload,
        headers=requestHeaders
    )

    #Throw a 500 error if the login fails
    if(pageDOM.url == "https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2FHomeAccess%2F"):
        return AppError(400, "HAC login failed")

    pageDOM = session_requests.post(
        CLASSES_URL,
        data=createPastAssignmentRequestPayload(quarter),
        headers=createPastAssignmentRequestHeader()
    )

    return pageDOM