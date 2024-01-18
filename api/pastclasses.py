from http.server import BaseHTTPRequestHandler
from bs4 import BeautifulSoup
import json
import lxml
from urllib import parse

from api._lib.getRequestSession import getRequestSession

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    dic = dict(parse.parse_qsl(parse.urlsplit(self.path).query))

    username = dic["username"]
    password = dic["password"]
    quarter = dic["quarter"]

    session = getRequestSession(username, password)

    pastCoursesRequestHeaders = {
        "Host": "hac.friscoisd.org",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
        'X-Requested-With': 'XMLHttpRequest',
        "Origin": "https://hac.friscoisd.org",
        "Referer": "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"
    }

    pastCoursesRequestPayload = {
        "__EVENTTARGET": "ctl00$plnMain$btnRefreshView",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": "mmzTBp9fvSbT0Gs49n+xVml9DdVZhC4nIiN32x8Th8dm4aJxR++mKZEBKpc3/IRhuSKhjTbeUuhvRLAWsqBu8RzsFMd6LHoJpeaEWQdnvBDR2JYNYWHfKc9dw2p7k/GPpcsHROtbAXn+XhEw2ivFokjLfcg/gok+zGKi7igolsvKjGyXeqtHrLM4SAzekUxZoCIYptD2QHJUyMp5fwwpVktFnWQF9Qc1SlnHUW1UDpQ0QWgNwgaPac2zA7Zs9bx8vACd40/nYQAvEmvUM8C8fZCSjWIX69I6eJGWvsferBuT4Hm3iwh7aepSfbxK9yWlVfpZNWXSeXBdX+rKf79yvTg4jxq36it9FNrwzQbUpag2xg9WO3BjtotRdfRAiW8g5sr4ZcqAxERJcnCOI87ZRPlJqxoMKmyEXxdwDkIcUaUdxVpREcoG/ts3qhTwQJd1rq+ZmLFVUGlpGwY+F3EV/8PdKnQ5dY8MEdod1IvHw4l4Y+NE4/xXExaYieJBuf90FX8gPzXmNiJ/QO+fjhWts4E3/qcABGDS80qFvPSIOM8C8S1WlW84W8EhJLnAJs1vmW6Ll6ufFpeBsYwGNmcDk8bYGpWpKpSZycr3j6QoQ0f0+o7CnHelDwDI5ttTH29s/crN76kB8a6ReS3dm0XHLl8YjIha21Nlf7X0KrNIqo16FQpMxNz96/R0w4UzafxbUh66yEAUqN0LXQXIrn9U9IM4HkA8uyC6nSBkOWM+ZHr98JCiXoV1o4mhdZzcFCgX2mPb1FP39rnxxOkQ5vxKGK0dOnUYYQq+0WNrEv0DlP/l+P9AL8tTtF8rxQKGGSP9xkmZSGvqh/UwPmeFhApDqauvFOiQrj8FLMxuXjnZ79aVLlVxSHR94Bfydlwn9v17WHgINhrNPORMfzsrZnm0ZlSucOrzj9UbVC30IvvlSt/yjZx+ii7rGnf74tVYd5ajRsVkhwntjgqKZ6TPn9ycbrGeFYMeVxOoSHHF7GG6xdkFyQ8CDZ/hc4c32B9DvcEWlmpzbNl/on+x7qPYevtiIkLtI++HynHhWN+J72kBljs0VNQVkg5Y+MvggR1MOAmJj96paPtJ2iHvS5ew5xGrUrlYeQHHu8BzPlIEbguwMuss4RxI+lLnVGQFWLBjLVwj3ua8zdLS/2ZYfJDJbofGuczSpyo3oIVCkpKpfmpWCf7Mhcx5lbjthYa3GQ0pOsYsoiHRCQiJM+Cm1R7XMxD1vuq0p+xPgmFShR6wS8XkFM2kQZFb/stG04hsyJQ9ASkoix2ai+XTXY7qCOW/Dp6Hl5B9gL0+J6qldyG5HKNSwRNz3l+KWz+EhdrVM3NtE49juNYd+I6H2WHg+J+jNWpbgR6IE0x7PwUmZYrs7qALSO22RkTp+wR+6xKkhtxG1edNDofCt0CArl7XaHPFWb6kHlDgeOedivvZ+RbWWS4YdH5pGIKjLltGGlOaUTTlajmT7GfWcBfYXbv0FKBgGPdsQG/fkF3SrEK3+XyyNrDA0J4=",
        "__VIEWSTATEGENERATOR": "B0093F3C",
        "__EVENTVALIDATION": "/rgmAwr8CsZaRCA/aaNF5VVeyABCUgS4L5pETYXq3cnDeyS7ePOZBcBW9JTUSRLp3rcDQVooVf/XjE+9KfbTwnK2iunhNWB+3ljiiQ8fANEXs8lA/LJ4wefyfq/BPs3FqR3vYMNH/QL13yQmb+EuDNQW+i836FgAEt3P3dDrBlirP4xlMvQfUC+DClJp7pEXRpwyoeIkj66Q7fcWOMg6bGnC97XCLgUjF2wvwpy+nMfFtDgHfXYynxnUwXTA5mhRNLiIgWkF34vnIiPOWdAI8IYlLJHgVllGtQYmofk8a+R9VKyrmesExNfooK2O5hyKODucqoUZp+XS2yv85YloyFBX668d4JqydUVAmZ/WmaCzjxxnU/6szcsMH/Zc/osicZmj17Hihfh8twTAr2WILiWnw31KWSY6HWboO2yeVO+hcvP8Ul4dlmx7cW02hM24H0JjqzSKBPd6zWinZZl0WTaigo6GHUD8P2SAn+jeVyMB6gtX/dxtjJlkWWN/fSU8Aoanavi39I/8kZBOCJue0rgkEu9ZHtGcz+0aM7LWbdoA6q3vpEVqz0dMURM4x8O3jXv5lK4aBy41mf6740aFjDJWYc0ftHdK6hXyJjj0Y1VAdhQNyUIrJaiyVnqY2RrChRRyfDcwEV3FnUSrAzRwKLjtZPtkNOwvScVzpGwNJ8qQrYDmb3Y3XohTd3VDH41bS/BTpN5lLI2dPW05dnz0R++w5K6NZX1RPwd4IcRs49aV2UvjYeTs3DEhGx3Zk3NMekgUjNjGP5RQZaCO7TAYtuhidRk6wR+1AaBb69e1zQ1RQqRJ5VVOy/8nMqlmLK8ln5CcLd0z0MWtY418y/Hyj4ppaZGjaPAXkQIl/83suL8cZv/ThsNGJIo+d7X+B81hzZDUcmV9dyjbs9eCJKl01xwUCyqcRIWmUB77h6raReoVF80exy0qX4m/YStUziW1f8F9FWqyhrvwo/Cv7Uikwmhdg3FpMc598M50+Fm3MgnxUfIEINxP1BgjFMpKjk85KQzqoPdzCQ4P9jRSCtwlmpAffHr5Y7wmzz1HmEcnfvx3xyk6Wh3SzT2fCD7mHRocjrLDUxyMxYMl70ZW3YCgnVxbm7pSDFG9Tz9pirGil9CmVnB09N1VolI1iAUuL1HoY4hqa/X/2dKwgsppERxlBxW1ddW/S7UYfCDdxHiNRAAzQIttKZHgJCdxeqMghSVeIo+CDLT7npjrVtNHMUpe3PwOZQBIPqgvQbjOW2vAIDOw1LIP2Nl/hW5EVpi6lw//5YP5it3rrI+9mtZZxa8VW4uBTEj5Ap4hbdfZ9f48HUqko6YHQP02aRcl0ms4GxwWQKtxfRNenpEWT8efQy4Lvs1oNwIe3QMGIPHXywzLpG6Rq+vbAhEvfsIZWZwxLhqis/LRXh3VjyMFNHQuU8uvLO4uFo9lgBVUxDmOtTEHZBUuCL5wuvz57/mBb1NJYaV5lphugwrDKYGk1MRvC+aPZPK/RfnwBJDIzeehi+53j+gcc3WMvuDbEUskDNnqjYt4HNrdSxfYxNdzynneT+JxoA==",
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
        "ctl00$plnMain$ddlReportCardRuns": f"{quarter}-2024",
        "ctl00$plnMain$ddlClasses": "ALL",
        "ctl00$plnMain$ddlCompetencies": "ALL",
        "ctl00$plnMain$ddlOrderBy": "Class"
    }

    pastCoursesPageContent = session.post(
        "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx",
        data=pastCoursesRequestPayload,
        headers=pastCoursesRequestHeaders
    ).text

    parser = BeautifulSoup(pastCoursesPageContent, "lxml")

    courses = []

    courseContainer = parser.find_all("div", "AssignmentClass")

    for container in courseContainer:
        newCourse = {
            "name": "",
            "grade": "",
            "lastUpdated": "",
            "assignments": []
        }
        parser = BeautifulSoup(
            f"<html><body>{container}</body></html>", "lxml")
        headerContainer = parser.find_all("div", "sg-header sg-header-square")
        assignementsContainer = parser.find_all("div", "sg-content-grid")

        for hc in headerContainer:
            parser = BeautifulSoup(f"<html><body>{hc}</body></html>", "lxml")

            newCourse["name"] = parser.find("a", "sg-header-heading").text.strip()

            newCourse["lastUpdated"] = parser.find(
                "span", "sg-header-sub-heading").text.strip().replace("(Last+Updated: ", "").replace(")", "")

            newCourse["grade"] = parser.find("span", "sg-header-heading sg-right").text.strip(
            ).replace("Student Grades ", "").replace("%", "")

        for ac in assignementsContainer:
            parser = BeautifulSoup(f"<html><body>{ac}</body></html>", "lxml")
            rows = parser.find_all("tr", "sg-asp-table-data-row")
            for assignmentContainer in rows:
                try:    
                    parser = BeautifulSoup(f"<html><body>{assignmentContainer}</body></html>", "lxml")
                    tds = parser.find_all("td")
                    assignmentName = parser.find("a").text.strip()
                    assignmentDateDue = tds[0].text.strip()
                    assignmentDateAssigned = tds[1].text.strip()
                    assignmentCategory = tds[3].text.strip()
                    assignmentScore = tds[4].text.strip()
                    assignmentTotalPoints = tds[5].text.strip()

                    newCourse["assignments"].append(
                        {
                           "name": assignmentName,
                           "category": assignmentCategory,
                           "dateAssigned": assignmentDateAssigned,
                           "dateDue": assignmentDateDue,
                           "score": assignmentScore,
                           "totalPoints": assignmentTotalPoints
                        }
                    )         
                except:
                    pass

            courses.append(newCourse)

    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps({
      "pastClasses": courses,
    }).encode(encoding="utf_8"))

