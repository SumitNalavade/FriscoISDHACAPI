from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
import re

from bs4 import BeautifulSoup
from api._lib.getRequestSession import getRequestSession


ASSIGNMENTS_URL = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"


def get_or_none(tds, i):
    """Return tds[i] if present, else None."""
    return tds[i] if i < len(tds) else None

def _clean_last_updated(text: str) -> str | None:
    if not text:
        return None
    # HAC sometimes uses "+" instead of spaces in this string
    text = text.replace("+", " ")
    # Try to extract just the date, like 12/8/2025
    m = re.search(r"\d{1,2}/\d{1,2}/\d{4}", text)
    if m:
        return m.group(0)
    # Fallback: strip parentheses and whitespace
    return text.strip("() ").strip()

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        query = parse.urlsplit(self.path).query
        params = dict(parse.parse_qsl(query))

        username = params.get("username")
        password = params.get("password")
        quarter = params.get("quarter")

        if not username or not password or not quarter:
            return self._send_json(
                {"error": "Missing username, password, or quarter in query parameters."},
                status=400,
            )

        try:
            session = getRequestSession(username, password)

            pastCoursesRequestHeaders = {
                "Host": "hac.friscoisd.org",
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) "
                    "Gecko/20100101 Firefox/98.0"
                ),
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://hac.friscoisd.org",
                "Referer": ASSIGNMENTS_URL,
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
                "ctl00$plnMain$ddlOrderBy": "Class",
            }

            pastCoursesPageContent = session.post(
                ASSIGNMENTS_URL,
                data=pastCoursesRequestPayload,
                headers=pastCoursesRequestHeaders,
                timeout=10,
            )
            pastCoursesPageContent.raise_for_status()
            html = pastCoursesPageContent.text

            soup = BeautifulSoup(html, "lxml")

            courses = []

            for course_div in soup.find_all("div", class_="AssignmentClass"):
                new_course = {
                    "name": None,
                    "grade": None,
                    "lastUpdated": None,
                    "assignments": [],
                }

                header_div = course_div.find("div", class_="sg-header sg-header-square")
                if header_div:
                    name_tag = header_div.find("a", class_="sg-header-heading")
                    new_course["name"] = (
                        name_tag.get_text(strip=True) if name_tag else None
                    )

                    lu_tag = header_div.find("span", class_="sg-header-sub-heading")
                    if lu_tag:
                        raw = lu_tag.get_text(strip=True)
                        new_course["lastUpdated"] = _clean_last_updated(raw)

                    grade_tag = header_div.find("span", class_="sg-header-heading sg-right")
                    if grade_tag:
                        grade_text = grade_tag.get_text(strip=True)
                        grade_text = (
                            grade_text.replace("Student Grades ", "")
                                      .replace("%", "")
                                      .strip()
                        )
                        new_course["grade"] = grade_text

                content_div = course_div.find("div", class_="sg-content-grid")
                if content_div:
                    rows = content_div.find_all("tr", class_="sg-asp-table-data-row")

                    for row in rows:
                        tds = [td.get_text(strip=True) for td in row.find_all("td")]
                        if not tds:
                            continue

                        name_tag = row.find("a")
                        if not name_tag:
                            continue

                        assignment_name = name_tag.get_text(strip=True)

                        assignment_date_due = get_or_none(tds, 0)
                        assignment_date_assigned = get_or_none(tds, 1)
                        assignment_category = get_or_none(tds, 3)
                        assignment_score = get_or_none(tds, 4)
                        assignment_total_points = get_or_none(tds, 5)

                        new_course["assignments"].append({
                            "name": assignment_name,
                            "category": assignment_category,
                            "dateAssigned": assignment_date_assigned,
                            "dateDue": assignment_date_due,
                            "score": assignment_score,
                            "totalPoints": assignment_total_points,
                        })

                courses.append(new_course)

            return self._send_json({"pastClasses": courses}, status=200)

        except Exception:
            return self._send_json(
                {"pastClasses": [], "error": "Failed to fetch past classes."},
                status=500,
            )

    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
