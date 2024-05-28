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

    print(quarter)

    pastCoursesRequestPayload = {
        "__EVENTTARGET": "ctl00$plnMain$btnRefreshView",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": "LrwyU5yvYWT289iRj/pNNwKZo2O+X8qP/hQ8LiPPlKbn5kpP642NF+6ouiPmZ59iZBEpbmk/Y5PZ2ovVtvcsI+da4vo8CJLh7oJKSCYXiTGc8Av88+cVihwOjQT6RELHYNgD8OU3B3uwxpTDdqcn4fyAuEkpQI+u9CEpYVqW3pJ4CdbN6AhhtYVi3ZwGqI/2uhthxYVLRDrxkoUMqQ4IHhgdYlCL5GKBQJkkzkCadlGgbOd1e1ZyQP/zcrADZXyTRV72Zs+Ky7V0GtdB5xVay5AD39My0OjQkNHKOanilrh0nN49tAIY1iV51cd9H40k01hNg+pAP98dfxsY5wG+AJjxTMc+qnimG2f+QGjGwhZOnn6+0PceapFMxP/7Ov70dYdbhprm6kvzyhw+0BE11yS8e35LMDyJI6/X1uhwwsEEkPQjKLnK2yZZzGxXL4grlVgAuAsRmPEJGlyRAnNMbQp9d5VU0AzJnGeqds9MqaRCxOBiafya8ZOY4TZFswdGSo+R0MmFeRwdUydfcXpgSZcgi6P2RGvIT6eKTXbmLiWAU3n/VB6Nz8xw2sCdH/pX1PPFwyzj/V+laZpgNCN5lfsnvfkJ2fW4Alv8nnWV087x/ki8TnxWEsZnDH+J5V2DwicbavJMW9rpYbrvdMVYoK7yzf3SJVOyekK6xGa9R3b5ea5MO6jMYgmOhG6Xi/Pi9TQnwjLNbtl4FaBBHP8aSbeIvHJmXtDKiBY4Ku3N432I8XgLuCd5d6AsZjh9DsZQqwsK+eSkU8Jeaos9HYgmzV6pT9/nm7+AbX3g0LzXqxSLWMiAYhl0T7cTVE92NO+i+A5915ejzaFCXPqxV7FSg5eyPS8R9l5lp7KquFAzPvCKKiHbffBd5OrPJqlwUjea+wjMi/wZX/dYuig1T08YadbK7ulzTSCmLtTmRHcMacpwGUBh2m/GSkrdrqC/KrfNlQQqQuQx/2ZYe48yMtg1ENxz3fI9NIW2HBfIyJ0lYJ9hW+wy2bmBvGnISCfWZRv7aXR9ekWaefXShMjpBrhcLqeDGgeBdMs8+ETaI+TZNhVIkg4eapmKKl8scvc0PP94G4qb58HNVN4MZg1pc3I5SsvfGSuTB2yk0Q7QJrrqPTpKxw1jo6KmBDejFzZbwlehQca6xUL6ijdVlDwm7eEF8VpjkD4cYCQO681MTofAAnYnLt96JDJETwNyHE73miEDPxEu4Ux1I7RcnIE+7vlDcyizSES1tLBi3OeFnZx3NiUcDD1G2PfVTVb0DH3XYlZ23eBzrZTFG8xjiDF1Y6cw+17wVukgHF+VE9lxbPghG6gRYDZ+/yfCefnKJQFQfpjrsBoDj9y/sOo6ydI1dT7aXIoOlqYhs+L4hxDfQI66Frs8s0ZADI9vor4zSWkf/Wjm1MN+ECFJCZb5Yw70Y+ePSqbsOAl7Q6MAG40wojjDjdjKd8RabvZ2ablNqmW1fu15pNte3i3xEYjhRsYkMQSrjfvm9KpCF0710c9XMKD9YTU=",
        "__VIEWSTATEGENERATOR": "B0093F3C",
        "__EVENTVALIDATION": "QZRbcthpynGiSmCxn7L1/IR7cCCDnwC9mLHizdX7DxflirHr4cXQ0mPg3hlqfFU9KNe0SMHIrG4QNqAR5ek8NvMcpQTdgFizII6o5EldpRec93IT6yzgiqyex8FBuviaM1J5p+Duar580PiMoERIrQ/+j9ZVE0n9OfF2dQxDV5LI+Rt5U53bnMRPgi29h0yW9VmfxhSQlV3LjqchFv7z0kGoaNuG8SEQ9a/qWBVdd1nsGWx55cBFfqAdVaOBcwe9DtwlP6SgBcj98AoGGP9OVMErk3Si0gcDLG4349O4QYQ+Kcxoi0ZNGCDHctDgMMnVrxWHxz0RvuwWmdKQ9VhO950DRgza9y8Qs3zSS4Yu6MB3Pfr0uz1XcZ4MkJlcn4QufnhtbQCZYGXkuUscPRE3Wc50yM0v0zP7e5YRogUxjVwtQSp+GVQ9376mmo4XM6VuVLOi9vncSYZj9Qc4MM8ZC3C0XucKJNPXU6XUTTFkqFechq4goUGy9OX24aItH/Fe5QR6jAsdlrI2kGJceqqWUhpQZlcALt5fhpjDGIoixeh0PtGOkT2kr98R0p2yY7Ut/MfZVIfPLyoE0EsYcjpXJPb6jyZ9pyEvv6/auJmwT4cXlVmpT3A2t9810y/VGmHeooSFujZSlYssqCx1YIsHfGasAhDYGYIPTy65u/lRWzyOlL9bMAkCkuHVOFFRfWAwFnm4oGYnr5MqideEwJAXaqxg1HoNh7HDJ4kabaFF711oPhOsXy5EhqtFz25nvrim6cw3Gc6wLW7Pw4WMXdhdXxlloX3v+GtsYSxM9Yw0GpfigH2dOoNkPjxsgF91qajYwI6J6rIygumV77NhOjs19TDL3Ec4B/jXTisW0VRevu+kkRHlyjH1PaW7yRAEXNYVve18THmlsi/g9QUJsVb6TIGEIq1qV3SBRaIcuvjC2Pe35S5nD9S2FY/NUxXGIMdkDsZWWI3PelsmYmnrGehHrrjUG+2CChNIvTtSRSB+FC+fY5th2VOfxv1fPWaj31jGwVbYCCCWHOYUWtwgTbIyTV9PtjvOm2+wI7KNFLynOt3cawNVvcTy2RuUqYE8hIHzWpk0wrSKIeFlyOfeUx5FP6oMiO5gRk6aoH2IZelTslt+9iPSV/XrfIFbJW0MLiFLlJXgs9ZUjRNyvMUETBYckr9200La897V7fkWZeHZ+EtKcac0/ZAEenK+FGuk1gscqBF6jwa7mnDnS7WYxYkSZFpXtQzhol+g1mVNpr03C9j1sbYYKKwLBEsxWTmZHVPsgoROYU7rXejoWaPMflq93zuWWifI0QMNtdCiBmFfYa88tlOvMddB7SmmwcUWh2chNYWSmsfM5gNhENRvPuVNOF6nBWcc/nExhsG/PCP75yn6frgS08wOdzcN5BGok2IBE5fOodCE0uLgMJXyZ4GIlbhGxwlLAY+aEq4qqQ7CYSkg//Feqsk2fqXUMuzB10naj/hJDBgcXlQVkJT/ZrE2rYXX53cm9Oz+ufeaz/mu8qla23WK5EQSJktFx5sgD/KFFnKcn2HYVQCjOBafH3A0Ig==",
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
