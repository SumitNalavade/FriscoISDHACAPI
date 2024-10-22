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
        "__VIEWSTATE": "nu2vba3D4zP41ItN9AJoWZPDWeEZ/KS7U22QhqvLdYxDIh0gFUELicnwClwDwnZDWA+dlkRqnNYO/kxqpFitkIQYAuKL/uweioZtLuc3TY7osWCnh4eCEMtO46gJDM1K30dnBTqGMueKJGR4rkqvgvMb7GIyGNzlGA1YAuD4k/NuZxjrYGuAIQL26aXTn95vkj6xqAUji1uuZ8+414VjLCXiDrlcqKuN/jIAweALLTNjTEq0YZOwx9sjkvn7L2dgb6v751GLJR1kDAZts4PT9qJ5adC6Of9+XVU671EjKsk3Y98vytZ9RC4MtCOospGEDc0jSxZ+gZ6EY2fLYj6venXrwwoh87PXymmRrrvBUoD3OXTN6ocQXs/+ps468f3EYCseugIsmu6EEfS29ALFAgD9V4WxuxUUQVN/9vd+rP2evtNr091Hvgd7BJrCR8Qe9gEdX9qtUqaCKZ5dmC5AAwlB1WyLKfTA7FGWzxnzTThnRWDUETavbf846/IvE3HHoF0MvPjKRxVp+tu6mDBoWWK2sWYh3nL85Ctp329BQsjA03e8O4V3JmHlpszoqs0tudJejZ2i+yrp7NQKzRo1UerID/Aulc6rADQXgb0C8ZDJS55vGoYM5sMQZ4CvzNxWiz4pmFtNMYyci2iou5VFCrvSmd1mrKz/c6ghoZfn3UgkYNL5WZiX0P7sLvcUEXyCgjpDBtWiP2PIqaL/fP+LQQlnJvXMMfZQUf4s7jR1fIJR6C+JETYSfm9R/maEPSX43ndTozXa3OoS/K8p+xGlsp2IEyrp8ZKPCcKdvoTMi2Cv/zxPeCsQt56x2NaJr4gcfNhqlVhVt386W254TdnZ8XmfU11MyrijGnyH2IpcyyprA+GBHY8uYrLeA9b8OsjpyOIviQnckLV282mz7hvgdMGi8vXjNVecr3a+EdH7RveHlsJJ/ziAbJpM02aZVPKQ3fuW2yVbTvZytus96x7Q/KKxMdokH/L//rZ4DIO0jShbAxcAldr5PvmPIbSwtBGEF9ZfhevPyo1LCPN09gQQclq17dbHzagQUah3l90pgLsSBXU9daTIPoMndev3X8sxPylI9SNc49Qhu3k1DeRO6xyB2mr5vuLVjmXd6c4NNrhg31pRqwZk3CV2V4VFZ2aAZnyId9zv68zYbuojAxppmWAP/k3dJ6w1UwOH4iDZjhvSsxOgAkEIZhqNLr0Hvk+oYXXPJWc3tpar0Cq+qKqg8RAvkiDI9mD0xn7ae04nZCweJHuwGaZVd+SFXroEgLWxWtU1zSGmqH0Q4QcM/NQPxfFfcBm5K06PtfkxUmd50jFLzzt6LvR6t4v5t09gszODoQiFLKkpq6kMJ14awPESxQo2dJMXZicta32bH3JgxRmFjPL+yp0AK/7gHjQhEc8ap/m/dXdrGFIzLiust7aNtXU+vc14FkX0QfqvwZx8ZLLl7Uot4RqxTmKii6ierF0pqW6P+vyOSD8MfIyL+tS726pE2cHVzC7t5JNkGcyqc5a8BxN5bqPAD7jTmwAs+fk5bFK4BRgttWo9WT9qPGmY4Y0d1UVUULvl9plHCttJ0r8pirPjaECDOVGJ6aHz1Avo",
        "__VIEWSTATEGENERATOR": "B0093F3C",
        "__EVENTVALIDATION": "cE9mC4DQzgsOWvS/8yGOMFIcT0tjRB/Qwxk3TLJZ6aBdwwc4gtkaLch8Vr+A2ps7ob/yt0gl65tVqQsFc5nG2jOU+a64i70g3vExxEb5gQJc3Jkn9uVLkBlqa7wzWYy0XcSd08gV2bfnL5s4nTF28MP1KEL/YrQWV+E+45wnnisyuiJ2Xo8XdE2uBkqf9uz+t/+Ni3peWMz9VUFWzAoKpvPAgsON33MrSzjPsXLgVIQzKkjUGhsRuChTMpU1E5YpFdsVuk1dUrF7QZz4rSqvjX9zHbwGiBsMgBSffyWpQ3RABaGyjGW28BmjFBigxmqTtVBF1g8znMc6fZFAuCCVKBwnP5jkRxaUJ6cN2eT/DZvfRIAcaP9B+XM8l+TH4LS12CgQkgtWNzT9KBj9MTmq+QMMX9hh3aREyfPQ2GPXNFq2uRXO6FP0etjUFy4/divjhYuHoV9XuBsvZhfoTUeNHbZXsVNLHAJN3tfXWB+uQ7uZVXWaHen/eJPsUT0SsuDsbjkSHgMKp7Y5TOgn4CzsoRDds9Re4MIjMESL1q9DvSY3WK4WhgEiuxBM2diL1+l5/IfAkxp5M+qMF2YZ1YkQF9Il5rldf7MKmdI4uYLqV2AIoqj8N3JNCk0plQCGsvN1l3uSveH9VvwRoCo8bcubV7Xvg8GYCgQ/JJr4TOHUEXHr0B3+xoItbfBScIIj3yFDbZ3vdG1qZ80hzjM/jvT8GyGaT1FI7M7CNbNLlJipuLfUUGUJ+ejZXrD7cONjYyWN3oBvWtEaSTGkKHEjTesPH/TR1PVhLUcm/0IFaXIB4jQrzhsep1QQqGqwb2ZL37881aOgKd86XVm9wUtrMlx/+5G4UPrcTNfNrhWuHeMNu2DJA04MuCk0X4j61/EOKPqntrZh2SsgphYHfC8n/Q28OgiavM+KD4XrRipvAPFY3Sh4hSFPwrAcpcssV4Nn34kLkBbMRVcjExJcwfhcrygX2C04Cbo9+Uy/bOCAm+ZncX1BW8+QlkzgxhB3lsHlOEluN4AT/6hQOWDMMIOePP39dqbjJ5QQMm75EtMD5XLHB2VdwsUXJeib1YN5vAEGk1YB6xsfFO1P27OFJXAj/LJFXj9QMhWA98RZd64CrMxwqvMzOwJM577b/AoPeCtGtNWBI+1EPX5f8VIHFsMd68Ny932VDZrdUFE6/0Zn8q2/JP8A+gbPfcs80nv2YqsKgTWWqyrL3XsyuZ1KaryBlonTkrrXe8AiomiB0k7Ht2hrbIUFTJ50Zp7SxPUWfOAjfLwl9IrtVFZOGAB8IBeBTmh1A1lKtvnri9CS+L/AsBlsX4Yl2eUeOQ9HfF/oRevbcBlCdysL1hKO9iBEJSSJPx4QAxfLFJ1Sv3m4Qn10HxbQ3Gg2CV3WOIUu6Rpyw1pHE3OwD27Bgd7TbNom0AEFFdR7oVKpkUJ6MpRm/zwYtEnTjBs+SEJ7E6VEST7+zGihG3lCsZN/AGkuY+E+uZlAWXCkOzmGcE5vxvF9W2IkF8cVyMf3oa2JiXQcg6eidEwEk0GSFqcISTeqM5ir+0abaqLD914W8Mk/7dwFq/kWNWGisSJyNvgmmCnIc4UUBJzCU56i",
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
