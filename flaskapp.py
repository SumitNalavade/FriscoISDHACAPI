from flask import Flask, request
from flask_cors import CORS
from index import (getInfo, getCurrentClasses, getPast, getStudentSchedule)
from fakeData import *

application = Flask(__name__)
CORS(application)

@application.route("/", methods=["GET"])
def home():
    return "Hello World"

@application.route("/students/pastassignments", methods=["GET"])
def pastAssignments():
    username = request.args.get("username")
    password = request.args.get("password")
    quarter = request.args.get("quarter")

    if(username.lower() == "john" and password.lower() == "doe"):
        if(quarter == "1"):
            return firstQuarter
        elif (quarter == "2"):
            return secondQuarter
        elif (quarter == "3"):
            return thirdQuarter
        elif (quarter == "4"):
            return fourthQuarter

    courses = []

    classes = getPast(username, password, quarter)

    for course in classes:
        courses.append(
            {
                "name": course.name,
                "grade": course.grade,
                "Last Updated": course.updateDate,
                "assignments": course.assignments
            }
        )

    return {"currentClasses": courses}

@application.route("/students/info", methods=["GET"])
def sendInfo():
    username = request.args.get("username")
    password = request.args.get("password")

    if(username.lower() == "john" and password.lower() == "doe"):
        return studentData

    return getInfo(username, password)


@application.route("/students/schedule", methods=["GET"])
def sendSchedule():
    username = request.args.get("username")
    password = request.args.get("password")

    if(username.lower() == "john" and password.lower() == "doe"):
        return schedule

    return {"schedule": getStudentSchedule(username, password)}


@application.route("/students/currentclasses", methods=["GET"])
def sendCurrentClasses():
    username = request.args.get("username")
    password = request.args.get("password")

    if(username.lower() == "john" and password.lower() == "doe"):
        return currentClasses

    courses = []

    classes = getCurrentClasses(username, password)

    for course in classes:
        courses.append(
            {
                "name": course.name,
                "grade": course.grade,
                "Last Updated": course.updateDate,
                "assignments": course.assignments
            }
        )

    return {"currentClasses": courses}
