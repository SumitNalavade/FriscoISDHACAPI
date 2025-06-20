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
        "__VIEWSTATE": "JaSDhXYfGa4RCUOoiApAwBtRAuN8cAD1sI56vhAn+SOGRgHZj8lbQJHCiR+3OrhgDbL/jDS6Ao4kJm2J5C0285pyH9F94V5LXbAGtQNuPyCn9yoJvmcDYRkifaNYFIcLnNhfrvSu8UEvD5rBQ/OY4kFv/wo7h7OV2Nmde4sP7dKuC4vC7ZRI5SXMjewuXPJdYpCUyW91yBKT1KRK+Ix4HkfoEXGCV/9yWL/VrXtP4CQqrNCoNCmEvIqvCo+/a1vyfxIrRLF5L+m79Gv6YBNS/uFHATRezyk5Hn9R4KO4ju4/0TC6G8Q7usW+e9hW9F6bR2/YqdxCYmUOvMsXdjpcnrzEAxS67mNG6i9N6Y1I82yy4Ez1RG5IyqqI4373AkAm2iboxNiu28KaA9zih4XenOUSKNoD9IVSHbFoKLaXI1WQMe0AM1WCxl2rUwKTM2A2Lss3MqFTYc6fzJzkshch5z/q4QUQB0k8G8euQbL1DmjmXvmsU93RMKMhVFGjq4t8Ee4yxPSCwY7iDeLoZ+6XtJBJFK/k+QI1C9PXd/85c+pHBwNdEE+98lnWHAGDp+j1IP1Y9bUpJOTTpa05ek58edgc/Mp+Owtu/Bz/5dH8Oud1+n/cU3WYftLJWFyTcUjsDVewPCXmWgQVrF14oWqkzeWMWvJH7ENsq4pcAFGdVZXrIF/r+yGlcBaJ/LjZpy4y3J+B7LYE4dG611YF2KWXk11P1LWcP/Cu2nb6KNQJ6xtPT3eO8YcD9Sqm49xB2gbRDJpmIBafv5tC6ReOBh5yhjqYO8vb/L+Z57Ua8WaZJn1W+FlVFAj6O+NQbMswfdkbfaFccXlKcF7tivsS38LDpkEiVF7JMhpW7+rMarVyaEEOeund5DFXf6ZrMnPsRECb93CAQSIsg+J8LpIWQxvYsh9eIduG31bSwScrG9zo74b0OeFbtPoE1t4vtasINFXS6MV1x0F/2kuyq76977Xb3cPJqMRqk65IPDu0QnVdZ3Vh6EzlSX4RkIgQYMF3tpOtyJab/vL9UIUl8Ti5sO/FBCZPu+f4AYbynrSAMHYvcBMDvxEHInpSSx76qiuyD73TUiKGD+Ky1ylC0sR2dZWBnVKzNwWcSBK1cryvX6gDuhsc89puO9eQgx4qH8CmdV3yj/bkEz68ASXhparQ8DWn+VGWeq7VzUW7VmWT0S8GMDLbnb7PVYIlqV1hDvIA8D46zMf2E4EHA5IYCUYw5Fw+6JP4k8IZ0Dg/14b48PfKVHF/U2X70WRq/0HF29fh3jgHoWvyPZwzxXK+rxgD9cdtdOpQZfPyjg1C0mn5/hrWuMrQNO/ZkiZfPeGHHIuIBmNEeeRtzjbxLsLA/62nelFHONztz32d60lQoVPYJZd0QS/O8pbT/xpXFTGQ9yInfDdnbTiQMr9DaSSMPn6+UaewyzQ94G/ZI0HyEh56s2ytkpgCMiztBKYxEdZTEJyPfa2nqe4dRKpRlh7DmfFnDKN1g/lRCrYcVGST1V2U+YdazRmpv+xakBKlhgnYYUV648iKQFCi42RBX42haDiHhwdtaf3pzltAlLrfnNB29rU/E0uujKOD91AUC/ajCKZhSTUHPJLN+QaHuCMOXJxprv91LQ==",
        "__VIEWSTATEGENERATOR": "B0093F3C",
        "__EVENTVALIDATION": "p2fpKeevNCH9fKkzWZHFUFLSf7b1sSW15W/rQm3H7ae+HA7DGmn+RZ8x5byBk4MAGrhMtUhwpFfT/b+GPjYlFbAurY+3SYhDvWfOMi5wkpXWw1a8jHXkZxcSYP0IZK2SrNky1xmSllBUn696IyD8MM0xWZDVEVTIp3QOSxAYGY2X4VTwOGOngu4/hNxwyVyHcT+K3r022oZUEoeXsB7xpnZUO4RSJEyiba/ymM9Nm41j02wBNiW40hL2DuGaCwR75Wj/jfl51sF6sqFa6krbE3C38i1nfehdgy1HzsfiPOLh5Zv1O82s3BEybUBaK4Z3gYrc863QnO5LYoTT3NCvrRSaOhK3jJAp3XbWvqIjWF8AKdor5tlhmJT/fEJ0Crg9wYZxCNGWehor5nxrZ85FhDp3TDlk7p/sKMGtM12XfkVohVNeCC7YvAD7LoBwUms8cCZEthgnW7Xy8ItztFZmwqpSBCPo9+GYXIv7vox9y340tFXeRYch+/R906EuscsbrSRcbA7QBg56SQ48AiKJoSfCAVdQmpvA5KlPwcMmw7x+1I1quMz8qdbtlyt7tkySXWON7cRqfIIywAmKoF/rkAjjZ37kWGnnHcu0qgp1nB5HXMZgHoIy/3SxL2SLxYWznQtzguzgfoOhRTbpbVqMhiXcTWLwMtC4zIPKei9ZL8Tv12X6nbPBPAmtrMg8kucI9YC/vc5ylUlx0GzvGrS+Q7iQ4PV/3QmLcC++v2zSe4T2Qpqud6sK/AMLKWkMGOC+fG43Id4tx0g6kPGALiSkzJpa7ZemWagIkwuaOlfGVNZOfIY8jIcg9ygxd9FOWEj/6Tthsd7h6NXTrYoQud1dwpCe+zdSYlYqoqhf15OHNQF6KjSmauvInRQpn2TgZFB3n5Tdsd7oXF4VmZZ4asBjjS7v/gEPzZq9npQLuQwkSBgrFa8ZbtcOxYANJSp+eHkEgszmxPl9Xp9mNKguJFmDlc4y99miDF+Qpeo9ZcM0U3hoFk0xtHWrA3QWnLBJ0QStQ4oicYHcstoeJYjgR0MzC66aU8qoQbGhXkh9ieDdK9/i3qpXSHqf0/nFuLzIPKOry5DRS4moTJNFwURQ7mZVIqOFaIoo1mjmo9sVk1q6eMq3YrjQj/2GeZzxqrKnD77NRJ6mVfcRR+e6eara1bfY2qPcceULzI+U32c9Viab8FsKFk+BUANtgdb/UKg/pRK90jXeoJXRBcKdQkO0z4lQtkG0sxR5ltag5fvAeXBdKDVCN0waer0WagoJVV74AMw4CUt03/2/VIsKtcJHRNZi5L14s10oGubjSxH5SqbggXzfgGbm+WEzCuHKuanBD4DaC+lp5ee4WNSHl31fciFEBaGSU82DDt+6LEQehvXIn3MkOFxBe1+ShBlteIWO59JhZ4ZryKCTf5Z1Ou216O6MI5rozQLKL8tbFirUdgFv4a2CanPutY5edc8xr15dym0NzBQzGcuCz0oXABUAnimX241B7DN+JelASvHilVD7vg6elX8TncN6DRh/EbSQ1JMOeoY8CLOhfCcBLvbwsiRCVYNlb/Y5fYgpzkLW8Rojk+U/OSVDpzrHk0/hgMPjRW+m0yxBO+IMT4fxllLRj5Z/Cg/SoRct68u9bnI0PUva5tM=",
        "ctl00$plnMain$hdnValidMHACLicense": "Y",
        "ctl00$plnMain$hdnIsVisibleClsWrk": "N",
        "ctl00$plnMain$hdnIsVisibleCrsAvg": "N",
        "ctl00$plnMain$hdnIsVisibleOverdue": "N",
        "ctl00$plnMain$hdnIsVisibleUpcoming": "N",
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
        "ctl00$plnMain$ddlReportCardRuns": f"{quarter}-2025",
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
