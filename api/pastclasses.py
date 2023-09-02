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
        "__VIEWSTATE": "exmuYmgbWSLRBv+Es51hUEX6rTfi7gOCO/ggi5NlEgJreaqqfhZ6jg5ny7CggLHjSXAMUcfp7KTqKOyPirjcjNwX76+zBJlM8OGdHEm/bgFpW/zMRgsS54a1Lcg87peqKHsjBZw2Vi7pT7mgFrdSYl2b5lK1uirCFmM0kZXE2nL4RsV7iSnuCi2smG3GgKJqM7NI9kHHq+wraqnpGojSkdwyUACfCNpmyHQNBw+C4CekU+9jRivsW/6ytDW+nRX7dyC1uc0f8kIx4gN2VDwnV0pgdaye7KxfwmiKDkY8WcRxjWHOy5KV6MHbqyb+sWP1LxA5H/QS41pmRpz711/d3jBR6I9Sokk+foleUw2T64KYwjnrE5Dy95Y3EiKmNtwm+d//0z6nMZUX3VAJPsggE07Myfr4McBRX0dKXjrXzmFffyc7IljdUrAyaOuenT+9zgz2GlCZAOGMSidLO0g7kurBXJIlIujZJzmTB6OcGevJTvvp9ii9lTA8skM+3L7ckD85rOMTLGnvXSrXwpGwG8kpKUBtyZZC4GIDPejjXA2nPPcsBWsrTOzC9Izx7r54eiOhxK0ge7P1Jh/4xSD/VXW3YYiu7Uxs4Qwm6a9aLakPwm44D7HysMlUhTX8ZtjSWBrv6nadGwF0RVh3/Q966EwxlR7S/k0fR5czMK+uEDzvl29vmJ22apRxKvbw1+BYM6/1A63ln32dbVsfSQgjCjzztGsXTMEZQw/lG+BdxzDuhEXkMA6iNdSxuPlB3/JTLhkAigYAAvICMaXUj2otuKCsxbDBy1Nm9J8dJ62cW5DWT63nQ5EnV4yMhR1k+2qvVSxAsw3i0K8XTIvbKLj70Hdrk517U9msLPRPLtTGjZsJZVdZH57C/+wGyiPwlnLxr6GhWBw36/sjFDzE0IarWT1FM9QI8dKp9en7QKE/8J7v30H7bBvpMALwmcO3CSGvJMyoVZELdljStRu4ikch2SxkcbqfsafujVvqZY+niHmTZCuzYtCID5r68mxCTEoR83Z2OSNOP5C0lesJ2mRTr/o69pZsopEpT8jP/W0f/uK5PfOOYcv0wd/tvaDtau5sOy+6iPcs8LcT9205zB0SDiBjX2J9shEbkhbohNeYs9zOgSe4SauY+IsJnQdEs9bFSdBsjBjdvoA/1VO7Pq1g55e04+nFFqSOl92Ev048FfqZ7uUvftUt8LC3KvIdew7oiuR7csh3U+UUBawX+1/up8+pK2OX1gxyya0M+n6UbC8a0wSxTUU28poAqJTLowLG2+10GytUr0qPPYt2afve+xBjvaGYQhRfWDNvb0SuVVjIbCeXKlr5vRdgCtVl3+6D595eFyH2WrU6GnrbW/jUcBXP8LMYdGtAqqROM40BQeFeXduILokLt5AvJjlxfjeHWmfvah0BV5Dx2ErfXoJcMOVJ6NV6XHRy3WfRRpnr26uUjx4stQthKGVL9+Xk6SDzyR/Pok073Y9X8dQjagPo4BDZthltAk25h+J0a25XPAy3Uw4Pqwb2lYeGrj2JZVqHBkc1LdbPlPN7er9EBS4Zr9YFn5oe/5zNan6F2Cc2NQ1pFOH+bbnJgvO6a7nzB7p1d9InaBWTZ61DNqrv+muATHMXzwY0hXU2r321kO9GzVpFmeQDTlsvCx6sLGFj53bLcLpCHvqlDWq1ALff4jn0yQ8i/xu/rThGI+sT6AolhTYkZry4H20OiOENfKKtR0pCarb4vTq2Dcz3GJ4Ffp1K9j8qT5WIvvqjgrTg6grxpldtAjwIFfGPXbjwvl2a4glgl0JILzstnG1NfDo+AgSqeNCdO72/yDefHnkVCbRm/jY=",
        "__VIEWSTATEGENERATOR": "B0093F3C",
        "__EVENTVALIDATION": "VZp7M4DBRFJggoQc6Q5YJ4DA6jkcu/FgdZb9aokaJgRBsg7PrU3dr9EkYBFROnDZcLBEFoWqzv4tJ/sP2BOmq2W2JNBFedLLaSBZ1CJWoL6LgFDvstNHIC/d9b+toj0ffNjJa3kt1hSFwFHYfMmXYo/hly6zJG2VzjgisiwdYh933e0hGMhS6h2havJtKOM4ikEmO8qhA3v69ljNCtC9RA5DP2ywhBD/3mynnBZjz0TZRgXuJHperP27zVgDvbasJtxXa4Jk2PrZPtKqVes/fM1Qkhmh4++FCdirNx2MCk5SRIXxKA4n3bfnn342ukLGWrXxMavVscKFvW3mj3PgdPvFBPQKSK9VziBPlJAozJKFz/LeaU6ZvK2FdJpxHRtsRcXxwazKHmVWyZ0eCNPEhMX6/5tVWSFHBATwdtdk6vQ15FTGw3EskB8kjQqwrjk8duXX95ijJ/CAnHePmaTJHvavueJGhcq7470eJmqIU/94vjFq+6nzzkd80rNnlzK86lyz0IJTodtbWG3Opab4oAQ8BhkwSgZQDnAdh9VyKnMv1+k0lEirIw0Jx+WShprcAaMCDB0TBmuA77dEnDCgml7QkdTBLqnlwCn78Xjkx8ygVSHw70Ohob3mGbbUFdkevgGh4nJpTxJ+3qvSeEW0/hj11jAA8tPS/L4t73WgM1itAlatV6duTkkO3tuQPhxWENH6t3c7SV1tEcjvn8Ni7MbKsLdXUWlkypxkl31bfxPJ6PJiLih1eshodGzUlS55PBEPoY9fKE3nIWEVgEOaPoniR4YLn6RZVRlthryNlfxiUgyW1tU9qSBxeZgiWn2NltkPRva+oP1HrcKfDK9ML1Padxfu3egSWv6VXrzK+7S0YsBifnmgyAQ0V9AZGSTst9dsZClM+gjqHVVnc4UifybZ5m0Ew9TaHbokugqOw7jsw7p+99j/FZa76Xnffby6Y67L6a7FzuCLyknumWgh0vi8scqlPhawTQAwqe7M6b+dcOrEQLLs3bDGHuhP1vI76c0rOlgerPtJcNL8gh1ARYa97fegdsZjng/BM1FE/jBCa8GLH6AP6TS800rybBZxzIzw57CMAzj4dqgWZTr26lF+Ww+nl4LGgp7oKfPLikzv4WfbeUTTlvTQut4NwODkgMbmrU1T84F2PkXXOkw9RXQ8xrbnbCHy5fnaW2LWwZJpX2VPFGI1TOn7uhkuPVhIoG475saqW/HthwgMowBiCEZCkjpQ3oemN5nTWRMp4TCcTlPMQ+F+AcHEM3WE4aSVw+gFdAJDxmR40hS5yCIAHNZ+95W4aszIi4jF0DQl8NusaYbV0KMr185j39Y3eWtfuDisPz3ZMHXx/r+fZIq+AiycX/faPOi9wzfmaPUcZgJ8xbasVFmJglih9/1//p/sfFw4sl/sTpAlTWG2kAJh6IMpKogqGB2+52gyVlhOowVIkUZJo7K3rRHGWqqkne104wXhwS4bRFAGMqYoQ9M425SC9oEeoZTK+sAigz7Xj631y6MOj+teSghc+5+cDVOdv38UOQ9TwvWjdDFMj6973anIN+Z0CfM2Us41ZZXMLRJeAMTliTYSci0wlojgw5eM7LbzZ0i+N5mToWYCvZ7b8JIJw14jhzG3Yb0ZZLR7L7o=",
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

