from course import Course
from utils import *
import requests
from AppError import AppError
    
def getPast(username, password, quarter):
    try:
        courses = []

        classesDOM = getPastAssignments(username, password, quarter)

        parser = createBS4Parser(classesDOM.text)
        classContainer = parser.find_all("div", "AssignmentClass")

        for container in classContainer:
            parser = createBS4Parser(f"<html><body>{container}</body></html>")
            headerContainer = parser.find_all("div", "sg-header sg-header-square")
            assignementsContainer = parser.find_all("div", "sg-content-grid")

            newCourse = Course("", "", "", [])

            for hc in headerContainer:
                parser = createBS4Parser(f"<html><body>{hc}</body></html>")
                newCourse.name = parser.find("a", "sg-header-heading").text.strip()
                newCourse.updateDate = parser.find("span", "sg-header-sub-heading").text.strip().replace("(Last Updated: ", "").replace(")", "")
                newCourse.grade = parser.find("span", "sg-header-heading sg-right").text.strip().replace("Student Grades ", "").replace("%", "")
                
            for ac in assignementsContainer:
                parser = createBS4Parser(f"<html><body>{ac}</body></html>")
                rows = parser.find_all("tr", "sg-asp-table-data-row")
                for assignmentContainer in rows:
                    try:    
                        parser = createBS4Parser(f"<html><body>{assignmentContainer}</body></html>")
                        tds = parser.find_all("td")
                        assignmentName = parser.find("a").text.strip()
                        assignmentDateDue = tds[0].text.strip()
                        assignmentDateAssigned = tds[1].text.strip()
                        assignmentCategory = tds[3].text.strip()
                        assignmentScore = tds[4].text.strip()
                        assignmentTotalPoints = tds[5].text.strip()

                        newCourse.assignments.append(
                            {
                                "dateDue": assignmentDateDue,
                                "dateAssigned": assignmentDateAssigned,
                                "assignment": assignmentName,
                                "category": assignmentCategory,
                                "score": assignmentScore,
                                "totalPoints" : assignmentTotalPoints
                            }
                        )         
                    except:
                        pass
            courses.append(newCourse)
        
        return courses
    except:
        return AppError(500, "Failed to get current classes")

#Get student info
def getInfo(username, password):
    try:
        registrationDOM = getPage(username, password, REGISTRATION_URL)

        parser = createBS4Parser(registrationDOM.text)
        studentName = parser.find(id="plnMain_lblRegStudentName").text
        studentBirthDate = parser.find(id="plnMain_lblBirthDate").text
        studentCounselor = parser.find(id="plnMain_lblCounselor").text
        studentBuilding = parser.find(id="plnMain_lblBuildingName").text
        studentGrade = parser.find(id="plnMain_lblGrade").text

        return {
            "name" : studentName,
            "grade" : studentGrade, 
            "birthdate" : studentBirthDate,
            "campus" : studentBuilding,
            "counselor" : studentCounselor
        }
    except:
        return AppError(400, "Failed to get student info")

def getStudentSchedule(username, password):
    try:
        scheduleList = []

        scheduleDOM = getPage(username, password, STUDENTSCHEDULE_URL)

        parser = createBS4Parser(scheduleDOM.text)
        classRows = parser.find_all("tr", "sg-asp-table-data-row")
            
        for row in classRows:
            parser = createBS4Parser(f"<html><body>{row}</body></html>")
            tds = [x.text.strip() for x in parser.find_all("td")]
            scheduleList.append({
                "courseCode" : tds[0],
                "courseName" : tds[1],
                "periods" : tds[2],
                "teacher" : tds[3],
                "room" : tds[4],
                "days" : tds[5],
                "markingPeriods" : tds[6],
                "building" : tds[7],
                "status" : tds[8]
            })

        return scheduleList
    except:
        return AppError(400, "Failed to get student scheule")

#Get an array of course instances
#Access the Assignments page in HAC, extract the name and grade of the class as well as a list of assignments of that class and build a Course object
def getCurrentClasses(username, password):
    try:
        courses = []

        classesDOM = getPage(username, password, CLASSES_URL)

        parser = createBS4Parser(classesDOM.text)
        classContainer = parser.find_all("div", "AssignmentClass")

        for container in classContainer:
            parser = createBS4Parser(f"<html><body>{container}</body></html>")
            headerContainer = parser.find_all("div", "sg-header sg-header-square")
            assignementsContainer = parser.find_all("div", "sg-content-grid")

            newCourse = Course("", "", "", [])

            for hc in headerContainer:
                parser = createBS4Parser(f"<html><body>{hc}</body></html>")
                newCourse.name = parser.find("a", "sg-header-heading").text.strip()
                newCourse.updateDate = parser.find("span", "sg-header-sub-heading").text.strip().replace("(Last Updated: ", "").replace(")", "")
                newCourse.grade = parser.find("span", "sg-header-heading sg-right").text.strip().replace("Student Grades ", "").replace("%", "")
                
            for ac in assignementsContainer:
                parser = createBS4Parser(f"<html><body>{ac}</body></html>")
                rows = parser.find_all("tr", "sg-asp-table-data-row")
                for assignmentContainer in rows:
                    try:    
                        parser = createBS4Parser(f"<html><body>{assignmentContainer}</body></html>")
                        tds = parser.find_all("td")
                        assignmentName = parser.find("a").text.strip()
                        assignmentDateDue = tds[0].text.strip()
                        assignmentDateAssigned = tds[1].text.strip()
                        assignmentCategory = tds[3].text.strip()
                        assignmentScore = tds[4].text.strip()
                        assignmentTotalPoints = tds[5].text.strip()

                        newCourse.assignments.append(
                            {
                                "dateDue": assignmentDateDue,
                                "dateAssigned": assignmentDateAssigned,
                                "assignment": assignmentName,
                                "category": assignmentCategory,
                                "score": assignmentScore,
                                "totalPoints" : assignmentTotalPoints
                            }
                        )         
                    except:
                        pass
            courses.append(newCourse)
        
        return courses
    except:
        return AppError(500, "Failed to get current classes")