import requests
from bs4 import BeautifulSoup
from AppError import AppError

LOGIN_URL = "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Account/LogOn?ReturnUrl=/HomeAccess?SiteCode=pldlive&SiteCode=pldlive"
TRANSCRIPT_URL = "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Content/Student/ReportCards.aspx"
REGISTRATION_URL = "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Content/Student/Registration.aspx"
CLASSES_URL = "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Content/Student/Assignments.aspx"
SATSCHEDULE_URL = "https://satsuite.collegeboard.org/sat/registration/dates-deadlines"
STUDENTSCHEDULE_URL = "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Content/Student/Classes.aspx"

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
    'Host': 'esp41pehac.eschoolplus.powerschool.com',
    'Origin': 'https://esp41pehac.eschoolplus.powerschool.com',
    'Referer': "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%3fSiteCode%3dpldlive&SiteCode=pldlive",
    '__RequestVerificationToken': requestVerificationToken
    }

def createRequestPayload(username, password, requestVerificationToken):
    return {
        "__RequestVerificationToken" : requestVerificationToken,
        "SCKTY00328510CustomEnabled" : "False",
        "SCKTY00436568CustomEnabled" : "False",
        "Database" : "370",
        "VerificationOption" : "UsernamePassword",
        "LogOnDetails.UserName": username,
        "tempUN" : "",
        "tempPW" : "",
        "LogOnDetails.Password" : password
    }

def createPastAssignmentRequestHeader():
    return {
        "Host": "esp41pehac.eschoolplus.powerschool.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
        'X-Requested-With': 'XMLHttpRequest',
        "Origin": "https://esp41pehac.eschoolplus.powerschool.com",
        "Referer": "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/Content/Student/Assignments.aspx",
    }

def createPastAssignmentRequestPayload(quarter):
    wanted = f"{quarter}-2022"
    return {
	"__EVENTTARGET": "ctl00$plnMain$btnRefreshView",
	"__EVENTARGUMENT": "",
	"__VIEWSTATE": "d3L0NFudb0FySIP7sZa+wAEGsxehxZK0ezgAKEruEAeg8nMihx6ZHLT8y0fQH5Ya85K4kcmzXXYm8I4sWrXgCN+zGMSxPui4LtYz15kf38S0GHdIZH5Rp3GMT2zrdG/whmcbYq8EhGDmIfAtpAyrVEJxsBJVpkUvALfYZgJXHD9L8IZrbYu0KPKk8vRzvFD2cw2W6M/ACr4H89Xrv5FAVm00ya/PEznNhKpB0OxQPannvR/mC+H2ZEos1/bAoo48zvQc1Za1s33tdmxod4iBK1cMO9tR9WfkGBrUJekMnNWqnATMaSEEQZgK08d5PDFh9dyfoo9TeNyJedxMf1kATkNyRlNcuSTck6KhA1g4blT0K0d6J02MLu8iG7r7NX+XM9x2oefkVvRtDxoCOgFEfKh2l+5NTtcAwk4X/cluaRJIwcjPr0YCi31doZudzN/oB2nIRj7IKWamC8BBTtRjHnsJR15ulRo6vkeRhzzxHCrYCfDsqIdeIUpPRxNpGYQN/2KUt5VUamnb4TIvUSMsF+NUzRvPUv+fQBsIpk/sQyEYZuQnBUCkUjLkRyejS1e/ZVbE1dj+5Z7vt/X4ZTfX4K0cZcOs34adfNwEIseukGR4FTUZncYufc2IKTWaEv8/SXe84Or23zX/ecGdt5Ymml4zdkN1wPO4vTuPvj7e5vtlnKHLFGmaLxK8q//hniVOKV4Cv2Xld8xCAkAwA7o4YizlnK7EiyuJqLxhqdSoVM+nnTWRIafMGFfP1yOZuJXfKIlkjPJ49FWMVIm9hviXipJ9YilVUYyqhuaJsU0k6kd/eFBwB6qeBkiqr4Nc4BzDdyjA3k59YWOoyYhXwAAapcTAPOiuhdptKEL43rTiAtLnUAFyKXfRVUYv6h+s/qymNE3rIMWRS+8tQD9VMaN0yO2eJUadMExoPqC3wvMxWGqyta7fhpXwcVLFuY2J+4bsf5bmh/exU/B3oYAhkWiBqgkyvxGLcuucZTIsUvp5ZiMPK6+muT8xEYKLWSXCTNQ6f/R1DgVa1AI5yjr3wlhWhHX9phyoGdwzHTA1Llur+ncuHaNNdtIsN/ZBjbcl5gWYbaAjF39bPJHkoHoqTDKF0ENZrW8PZU/DQ2h04r4MIBlrNMqO/0wqUkUlC7cLNgwVUC4DHWxDSBOsSDJC93IkvNcXI7LfreD9uCppcoTWIWt4X7aW4EMnVR8eCo+6pbGWX/omAskI3Ta2waBtCuXDXwSqpNQJF6N1Iho6KvwdRqdyU7TNYkEHrusu2uQ3DrsO",
	"__VIEWSTATEGENERATOR": "B0093F3C",
	"__EVENTVALIDATION": "4l2Qo+aXEZCdi2ZLaDOqWgPfcUD32OczPX3xS+gt0w6Jpgaq+iOFVt9twiG4hI/WQlQ3x4iM8qcBfnOcmQkDHLqbe5Fl9TwMTK6hnBjJ/2x3xKGE/JjbV4K8G7rKVmTvTMqgXEg+NDdr6r1WsUWtakZUCyEFDOnU5fC2LaTmG3DY7NHYAvrUrGHrGnKYPQ8hAN/08q+Z6OXcFijweskqvNSw1Qjiw2l85HaK2bVUcZjMZlbhx8g+gUhy08DBvYzxnTJjNExiTTN457rxPEm4xXKG07MPqY8FzW6Z7v+g63hy/5fwPSS84T+muBt7Uzrd5gito2j4pb38Vc+FW5iPryRSNx5FUJcKlu7yjnMwHuvYoTlYRVPfhx8xZIgIDwhkiiiyYuDfGFI9ZiAy09rwKoZvTtepa9JAzY39w38hOCwmPd/VmdD6BHZwVkno1MxCtgCL8kX9Am3eDK0OkKg2AMryTeFv3S1qi1RP01TuUrUgApDGzaicWZKcDmZdhza7uh8fwCLUNCMpHszdw5vRzwKxIqCgvgv9rUBZfP2O4owUY/jXYE5RGdZB0zQBzMDcOvJa+1yy9mCfU+Q6hFOdjclVPONGWtkgl5Mbr+pGwrNGJL18aSbZicG2e12dgRiWbkm2KEfb+sfQm0MENqWGN6BrtkeKuQSvaQtHiqbemVoy57fEEKBJO38ZGXoR2mNOi2qaDfIBXEWBs8CSSbeaXlpDHS3TNCSWeEVJRj+P5LHIdRkblWR0EdhC1+GWKJhp135j06JvlB/c9jaQqncsdbI581IF78S4/azMH/pmP3uuW7qgWxeveRvjyIOOe4wUSYx8NLSblM5aHcmCizHMSAUm+uEjZJdHyWKMUzqrJIaGQOa5C4uHkhSEi4i7+/LCDHUeWAH36xlaJquh48LM8dU713RSdEdSPc7fIfWxpW11wrWIcZVK7okpOu5c2BQcL9jwu5mRV67DdoJt0cLbhQretN5CFajBA5ewStNqZig5cwcQ/prHYEGx4eeXFPKVP2Yt44TsCLL1QjPTLMCltSzcyZBrxb6gi1a+YesEvaMsG6pGDFU9daKSuIHGixwR4oiMcLYkaGzHShsxp8SBpH/v7f9f9M47BX9o9/McwrFZ0yGA3J1VSkZDAdTM2CyExcRhc/DgHjrMxAmVY6aU2d3AA6AisSn82M/AsT7JYZRwv9hKanjfLi4qLDoi46ysmKAj2+UPMFBj9rRMtol9YkW79rJ3auBE19GnaNVt0KtO47o2liXAO0L67BQMJjKiRMileHZ1Wm/MJCIWwvBJQNUPQFcABQvr5TPoNFHC3xfGh5Kpr0x7BY6Jabq+B0ZxsqWx48ZBdSn70JdPz79Tz8Uc4YHoULEbnuiquyry12Jwmpnzdwjno0PFkPDE+DXoaNzbuv+lwJZDMtBMdVnUmxvVbUfBSvxnnwmIwAzcnRCJZHgtHlNFQTyo2quxD62QqgG3ErXup4KdLHdD7sLBX0Kob30cMLgjC9yaxdbPOFHnaW1VP6lLjjdkwTLGeknqo+rqiFfswI8DUmV+O9h4Gw==",
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
    if(pageDOM.url == "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/SessionReset?sitecode=pldlive"):
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
    if(pageDOM.url == "https://esp41pehac.eschoolplus.powerschool.com/HomeAccess/SessionReset?sitecode=pldlive"):
        return AppError(400, "HAC login failed")

    pageDOM = session_requests.post(
        CLASSES_URL,
        data=createPastAssignmentRequestPayload(quarter),
        headers=createPastAssignmentRequestHeader()
    )

    return pageDOM