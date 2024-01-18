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
        "__VIEWSTATE": "OSrbqE1ZtKhFPBzxrPCyscRBy8KuvIF6VZTm0SKVmgOpG4u+0KsuNC4xKzTjRQ1F+tbLRFpI5JLLTfWwYo5/7InRZzSCnQlEcdZd+33PktJlhhe2XiNorSTwHi36mWnybbP46PHBFh8GiVViL0pdeVpuA0q/Iil2Wec0t8GgWMamSUwJpX0+Uh1MqV5hCSuJMWbsRuL4t0V2dOQ2f48+ZH2ZPPijeSM2H8b9/+Y7xkCWq+tltVpKZ1S7YNM3sDGbSrs74x+qkce7gr3wen1LUTnugQH862/HAY9MIALfeX6KzDmF1VItmp5M/9eC18t9qIReYoi5o/7qNMvS66giQ0c+376d2ETgE79y7PaaVfr96k3MfNy3rCFvaSCCfyqzmZ9l1/pUfNURz2tUEIoWY5GiILgUe2Wr/vn5dv72enQx3p/MKrAf37GVM16uj/pm5zf1QWInhdVbSb1ouct0u93RkXkxZgRS6js0HuBD2u+vR2+32YritIeFtdiGCXqWoedq6NJFLC9+UFOT35s8pvlbLK40gguQZi0DeRsQq3nMQgN6caWNFBjY4LlUWz5e5wQ0HE3u65lL47JFHKXl1vqbYBdgMLir3x/FDfZL6I3dHYZib1dMM3Q8K/3v/OaeaJ8KirV8D9Yvz1B864vZk7fiO8OTvZ5tfXZukU8jKmsWbkRMP5eq43/ARfpVVU2JSFQJQw1uXfDrXu9+81MKZIIitTRyafIbjo2adIQQ1QggHK8AbxIKw678uscovgRgBfWhY17tpiaVGMiUXRQUA4QXUyQA1O3qbfRerm4O/Evy34i+SBcTFckOFi2ytausPZTtgTTtdVww1AnhuCly75my//DdLhRpy7vCdHdaclRq35EnbfgWAQvQq+wvuwb594oXByIsf1E51iAFHYqcech0lyn6o/vLLvpg5hWBQAgTNZdNZz7IdIfesSaairVEhGyGQd05eUEKXXT2i8f7+Bq38GNjgHcKiyLdernjC8k/9w7ugdswFXUf95b/TBkrNs4wq9bFPQVMzW/rm4cc76cm5k2sIKsecg3B55M1ppF9qxHd4bJBHFViUbZN+DbVLMobGsR4sx0CckpoyxszYNo19kjzaP0p+jrgCxEHS8ipNUZY6+VFLIKGHeXaPXSsfEo2/Tz5+q0QTMtxZZqMhwCviLq5WhW68V0v+hnzIxBnXQipApkVblgkIN8HLg/uF0BGFxiYMeX6qe4khjL2YMbUzP731Ysp+NwireEX+d40eElh4ElYFy897de0wX+68dZhnKeKmqkMDFXaA9dW3wtF+p8/CSxaPK8DYAlmEbhbOgw+fX4HXzTFFWDbg6KH7K/sfC/jKvZh77AKQr/fl3WLIfIksoQ4w2k9bAmCewAEZeVUwBReBH4HU3WW6RzkUjfnbQWi9w5g8CsfkTWQZjXvrl1Lt6G3063AnH+uiQkxIMbyNOusseMzqheW5lOlY6c0qyrhgg2G53Ex5REYu1cR/Ha4JX9qTTjHL6sdv6w=",
        "__VIEWSTATEGENERATOR": "B0093F3C",
        "__EVENTVALIDATION": "V4iA6b3yrU5FjXbARbksovHtJ7A8gGO+GO6cGpp9JQsI3MRIQ6C5ipmBM80keXq/bzUnodHgBnLDIr/i2XjKNMiqKM/ys1rwvDbKi8PeQaeya9Vz5OMIKCfBWftesZak3UVwl25YDTjhTnYBySqhS++hTm1xocgBpfRN0PLz+i3hsflOPg3HXfXDi15vkY+Wq1ODbEGGeJY72/vrzaWz+MudaLV+Q+altDL8Jt7CtkcelJThAc+U7/aVjsjzQXKZrXuqjd9Xi31BEtVC/W+DrQCPjobwxyM+eMZBfjASgV1mV1Mi8a7/P4tGaGwpMYjPuNAzU7Lhc/ahZrPxChn1gLr2SnxYiCNreDnfdOwZiVrz7gebnwGIApLHtXtlC0pRbjuZYz8pPg0EHxbQXhyvAmHNGIpR8a/08LCRg/Id9X03yLwDE1kbJbxxReli38wdGeECqUXo+r8hN6NtDvcl0WWtOpVx0MTHwEKN9brMMxkxKjHrwieWvqvm0U7QjtnEVFIOHZcdkpknZItgHO+qrIGfxbQmcgUAXt3EBFcGcjh/aQTgm99rGBDpgNBt8Jt8AYaz35k9pq13gcmpliK5SldXIz2B4p+wdzQ0IZwoSCP8TtEFwLOuwAPWs9fOIVKgXP815FxIHU9fR2CmrBMw//XFqkSejkcwuYf6B4mcWKHtJOAAb10eZ5T89hzpG0ELn+TLqoXCV48jo1J1qOlOr9itwi09hcQyJ7fXbiwj+3UoFvGzFdV2ngKlBTHlZBl9fQzLUxaSZnRrOZ1GS0OkdIOWTFZCYgHbdW5ZWNiljbnsVXSFv0WaDwkG0NS5Ga7CjU4L733E1W7+1lmG0iBvkIcyib1kUbZ3fl5AZWP7Zxr/rvaeH2uxKHbG27u12oaxBXCzwQMDfC8HILIdrgFaJSz/eqIuDSpVBmYAQCBM8IQ6+mDAP3rJqQ+KEJPAggHutc9U4f0Gnlg3Psq5GPw95fG+OHcoa1B31xheVbWsKrUhTaAgJnI6bJ5FqbNJuEocDGnw6MXACj29/C7iuCd6UiMY0tt1z9wTVbM6z4WZGwIyqAcBA6a99RCZ8nvTJIOSzFrpgmuvNWErTMxmnFP8q/6PByKxVvnfaHP2A/9jpwMlvY0s4xc+YQ8gsXVN+PWf/q4MdvCFX+D40q0FuOmB68fMR62Yho1nra4qTshdaT0jv8M7gFUa42mtjbw4NlS+MW5Vwr8w0O3lNTFKToP9AMiXFo8RYKTe8fANij7P1PnB+Ar410nMr6gpHUPTtxWqtoI4oshI2QQGZK+LylTqEdblFlZY4DP/vYG3KAFyMuZvmPtp6WOWeq/OtxBg4PfT/UV6xHxwgafxZScN8p8aAEGBxSGovEQj1Mtkhu9egGvZg/QWgZZLlLQITatP5wGkLdn0N8EwJMjeehLzAxm/4BeK2oH7IN6UleuPUb3Aev8nCJFKen0Wp4RdbJir05mxShnq4YzaQuqWxW9U/gEoclO2ktL2YpJjXXtBp/7EqxXgfSa+4lnUUq2tsKgK81COJuQb4XwMpNjFuB1DwqCpUQ==",
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
