import IAPIRoute from "./apiRouteInterface";

const APIRoutes: IAPIRoute[] = [
    {
        type: "GET",
        id: "info",
        title: "Student Info",
        description: "Get a student's personal information from HAC",
        queryParameters: [
            {
                title: "username",
                type: "string",
                description: "HAC Username",
                required: true
            },
            {
                title: "password",
                type: "string",
                description: "HAC Password",
                required: true
            }
        ],
        exampleRequest: `axios.get("https://friscoisdhacapi.vercel.app/api/info?username=john&password=doe").then((res) => {
            console.log(res.data);
        }).catch((error) => {
            console.log(error);
        })`,
        exampleResponse: `
        {
            "birthdate": "12/24/2003",
            "campus": "Heritage High School",
            "grade": "12",
            "id": "123456",
            "name": "Doe, Jonh Thomas",
            "counselor": "NELSON-MOON, LANNIS" 
        }`
    },
    {
        type: "GET",
        id: "gpa",
        title: "Student GPAs",
        description: "Get a student's most recently published weighted and unweighted GPA from HAC",
        queryParameters: [
            {
                title: "username",
                type: "string",
                description: "HAC Username",
                required: true
            },
            {
                title: "password",
                type: "string",
                description: "HAC Password",
                required: true
            }
        ],
        exampleRequest: `axios.get("https://friscoisdhacapi.vercel.app/api/gpa?username=john&password=doe").then((res) => {
            console.log(res.data);
        }).catch((error) => {
            console.log(error);
        })`,
        exampleResponse: `
        {
            "unweightedGPA" : "3.8800",
            "weightedGPA" : "5.0500"
        }`
    },
    {
        type: "GET",
        id: "schedule",
        title: "Student Schedule",
        description: "Get a student's schedule",
        queryParameters: [
            {
                title: "username",
                type: "string",
                description: "HAC Username",
                required: true
            },
            {
                title: "password",
                type: "string",
                description: "HAC Password",
                required: true
            }
        ],
        exampleRequest: `axios.get("https://friscoisdhacapi.vercel.app/api/schedule?username=john&password=doe").then((res) => {
            console.log(res.data);
        }).catch((error) => {
            console.log(error);
        })`,
        exampleResponse: `
        {
          "studentSchedule": [
            {
              "building": "Heritage High School",
              "courseCode": "MTH45300A - 1",
              "courseName": "AP Calculus AB S1",
              "days": "A",
              "markingPeriods": "Q1, Q2",
              "periods": "1",
              "room": "C112",
              "status": "Active",
              "teacher": "Poltl, Beth"
            },
            {
              "building": "Heritage High School",
              "courseCode": "SCI43300A - 1",
              "courseName": "AP Environmental Science S1",
              "days": "B",
              "markingPeriods": "Q1, Q2",
              "periods": "1",
              "room": "C202",
              "status": "Active",
              "teacher": "GLENDENNING, SHAREE"
            },
            {
              "building": "Heritage High School",
              "courseCode": "MTH45300B - 1",
              "courseName": "AP Calculus AB S2",
              "days": "A",
              "markingPeriods": "Q3, Q4",
              "periods": "1",
              "room": "C112",
              "status": "Active",
              "teacher": "Poltl, Beth"
            },
            {
              "building": "Heritage High School",
              "courseCode": "SCI43300B - 1",
              "courseName": "AP Environmental Science S2",
              "days": "B",
              "markingPeriods": "Q3, Q4",
              "periods": "1",
              "room": "C202",
              "status": "Active",
              "teacher": "GLENDENNING, SHAREE"
            },
            {
              "building": "Heritage High School",
              "courseCode": "SST34310 - 3",
              "courseName": "AP Economics",
              "days": "A",
              "markingPeriods": "Q1, Q2",
              "periods": "2",
              "room": "C117",
              "status": "Active",
              "teacher": "Dempsey, Patricia"
            },
            {
              "building": "Heritage High School",
              "courseCode": "ELA14300A - 4",
              "courseName": "AP English Literature S1",
              "days": "B",
              "markingPeriods": "Q1, Q2",
              "periods": "2",
              "room": "B115",
              "status": "Active",
              "teacher": "SHASKAN, ATTICUS"
            },
            {
              "building": "Heritage High School",
              "courseCode": "SST34300 - 4",
              "courseName": "AP Government",
              "days": "A",
              "markingPeriods": "Q3, Q4",
              "periods": "2",
              "room": "C116",
              "status": "Active",
              "teacher": "Huggins, Jonathan"
            },
            {
              "building": "Heritage High School",
              "courseCode": "ELA14300B - 4",
              "courseName": "AP English Literature S2",
              "days": "B",
              "markingPeriods": "Q3, Q4",
              "periods": "2",
              "room": "B115",
              "status": "Active",
              "teacher": "SHASKAN, ATTICUS"
            },
            {
              "building": "Heritage High School",
              "courseCode": "CATE36400A - 1",
              "courseName": "Prac News Prod 2 S1",
              "days": "A",
              "markingPeriods": "Q1, Q2",
              "periods": "3",
              "room": "A123",
              "status": "Active",
              "teacher": "BAGWELL, CANDACE"
            },
            {
              "building": "CTE",
              "courseCode": "CATE27600A - 3",
              "courseName": "Mobile App Programming S1@CTEC",
              "days": "B",
              "markingPeriods": "Q1, Q2",
              "periods": "3",
              "room": "XC148",
              "status": "Active",
              "teacher": "BUNN, BRYAN"
            },
            {
              "building": "Heritage High School",
              "courseCode": "CATE36400B - 1",
              "courseName": "Prac News Prod 2 S2",
              "days": "A",
              "markingPeriods": "Q3, Q4",
              "periods": "3",
              "room": "A123",
              "status": "Active",
              "teacher": "BAGWELL, CANDACE"
            },
            {
              "building": "CTE",
              "courseCode": "CATE27600B - 3",
              "courseName": "Mobile App Programming S2@CTEC",
              "days": "B",
              "markingPeriods": "Q3, Q4",
              "periods": "3",
              "room": "XC148",
              "status": "Active",
              "teacher": "BUNN, BRYAN"
            },
            {
              "building": "Heritage High School",
              "courseCode": "REL99013A - 1",
              "courseName": "Rel 4A OR 4B S1",
              "days": "A",
              "markingPeriods": "Q1, Q2",
              "periods": "4",
              "room": "N/A",
              "status": "Active",
              "teacher": "Staff"
            },
            {
              "building": "Heritage High School",
              "courseCode": "MTH45310A - 4",
              "courseName": "AP Statistics S1",
              "days": "B",
              "markingPeriods": "Q1, Q2",
              "periods": "4",
              "room": "C108",
              "status": "Active",
              "teacher": "Davenport, Aimee"
            },
            {
              "building": "Heritage High School",
              "courseCode": "REL99013B - 1",
              "courseName": "Rel 4A OR 4B S2",
              "days": "A",
              "markingPeriods": "Q3, Q4",
              "periods": "4",
              "room": "N/A",
              "status": "Active",
              "teacher": "Staff"
            },
            {
              "building": "Heritage High School",
              "courseCode": "MTH45310B - 4",
              "courseName": "AP Statistics S2",
              "days": "B",
              "markingPeriods": "Q3, Q4",
              "periods": "4",
              "room": "C108",
              "status": "Active",
              "teacher": "Davenport, Aimee"
            },
            {
              "building": "Heritage High School",
              "courseCode": "MSC15136M - 12",
              "courseName": "12th Grade Advisory GP1",
              "days": "A, B",
              "markingPeriods": "Q1, Q2, Q3, Q4",
              "periods": "ADV",
              "room": "C218",
              "status": "Active",
              "teacher": "O'brien, TIMOTHY"
            }
          ]
        }
        `
    },
    {
        type: "GET",
        id: "currentclasses",
        title: "Student Current Classes",
        description: "Get information on each class a student is taking including assignments and grades",
        queryParameters: [
            {
                title: "username",
                type: "string",
                description: "HAC Username",
                required: true
            },
            {
                title: "password",
                type: "string",
                description: "HAC Password",
                required: true
            }
        ],
        exampleRequest: `axios.get("https://friscoisdhacapi.vercel.app/api/currentclasses?username=john&password=doe").then((res) => {
            console.log(res.data);
        }).catch((error) => {
            console.log(error);
        })`,
        exampleResponse: `
        {
          "currentClasses": [
            {
              "name": "CATE36300A - 1    Prac News Prod 1 S1",
              "grade": "71.67",
              "lastUpdated": "12/20/2022",
              "assignments": [
                {
                  "name": "Production Setup/Breakdown Quiz",
                  "category": "Minor Grades",
                  "dateAssigned": "10/17/2022",
                  "dateDue": "12/22/2022",
                  "score": "L",
                  "totalPoints": "100.00"
                },
                {
                  "name": "PA Script #4",
                  "category": "Minor Grades",
                  "dateAssigned": "12/12/2022",
                  "dateDue": "12/22/2022",
                  "score": "89.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "MP2 Package/Segment #2",
                  "category": "Minor Grades",
                  "dateAssigned": "11/28/2022",
                  "dateDue": "12/16/2022",
                  "score": "",
                  "totalPoints": "100.00"
                },
                {
                  "name": "PA Script #3",
                  "category": "Minor Grades",
                  "dateAssigned": "11/28/2022",
                  "dateDue": "12/16/2022",
                  "score": "83.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "PA Script #2",
                  "category": "Minor Grades",
                  "dateAssigned": "10/31/2022",
                  "dateDue": "11/18/2022",
                  "score": "89.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "MP2 Package/Segment #1",
                  "category": "Minor Grades",
                  "dateAssigned": "10/17/2022",
                  "dateDue": "11/11/2022",
                  "score": "98.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "PA Script #1",
                  "category": "Minor Grades",
                  "dateAssigned": "10/17/2022",
                  "dateDue": "10/31/2022",
                  "score": "71.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "MP2 Calendar Check",
                  "category": "Non-graded",
                  "dateAssigned": "10/17/2022",
                  "dateDue": "10/19/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "ELA71000A - 2    GT Amer Studies/AP Lang S1",
              "grade": "93.11",
              "lastUpdated": "12/20/2022",
              "assignments": [
                {
                  "name": "Ch. 27 Questions (Eisenhower)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "12/12/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Final Research Essay",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "12/07/2022",
                  "score": "94.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Great Depression LEQ",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "11/16/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Annotated Bibliography",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "11/16/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 24 Grade",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "11/14/2022",
                  "score": "84.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Gatsby Project",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "11/04/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Progressive DBQ",
                  "category": "Minor Grades",
                  "dateAssigned": "10/28/2022",
                  "dateDue": "10/28/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 21 Grade",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/25/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 20 Grade",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/17/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "MTH34200A - 9    Pre Calculus Adv S1",
              "grade": "82.55",
              "lastUpdated": "12/21/2022",
              "assignments": [
                {
                  "name": "Unit Circle Quiz #2",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "12/19/2022",
                  "score": "X",
                  "totalPoints": "50.00"
                },
                {
                  "name": "Unit 5 ReAssessment (5.1-5.5, Trig Functions)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "12/15/2022",
                  "score": "X",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 5 Delta Math Assignments",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "12/14/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Practice Unit Circle Quiz",
                  "category": "Non-graded",
                  "dateAssigned": "11/07/2022",
                  "dateDue": "12/13/2022",
                  "score": "INS",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 5 Review (NonGraded, Participation)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "12/13/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit Circle Quiz #1",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "12/13/2022",
                  "score": "40.00",
                  "totalPoints": "50.00"
                },
                {
                  "name": "Unit 5 Assessment (5.1-5.5, Trig Functions)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "12/09/2022",
                  "score": "86.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "5.1 Warm-Up (Participation, NonGraded)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "11/29/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 4 ReAssessment (4.1-4.4 Sequences & Series)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "11/16/2022",
                  "score": "83.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 4 Delta Math Assignments",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "11/15/2022",
                  "score": "92.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 4 Review (NonGraded, Participation)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "11/14/2022",
                  "score": "ABX",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 4 Assessment (4.1-4.4 Sequences & Series)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "11/10/2022",
                  "score": "83.58",
                  "totalPoints": "100.00"
                },
                {
                  "name": "4.1 Skill Check (NonGraded, Intro to Sequence & Series)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "11/04/2022",
                  "score": "ABX",
                  "totalPoints": "100.00"
                },
                {
                  "name": "3.3-3.5 Test (Exp & Log Equations)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/27/2022",
                  "score": "63.56",
                  "totalPoints": "100.00"
                },
                {
                  "name": "3.1-3.2 Test (Graphing Exp & Log Functions)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/27/2022",
                  "score": "73.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 3 Delta Math Assignments",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/26/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 3 Review (NonGraded, Participation)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "10/25/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "3.3-3.4 Quiz (Exp & Log Equations)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/25/2022",
                  "score": "72.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "3.1-3.2 Quiz (Graphing Exp & Log Functions)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/21/2022",
                  "score": "73.60",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "PEC03001A - 1    Cheerleading EQ3 S1",
              "grade": "100.00",
              "lastUpdated": "12/21/2022",
              "assignments": [
                {
                  "name": "Participation Weeks 7 - 9",
                  "category": "Minor Grades",
                  "dateAssigned": "12/05/2022",
                  "dateDue": "12/22/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Participation Weeks 4 - 6",
                  "category": "Minor Grades",
                  "dateAssigned": "11/07/2022",
                  "dateDue": "12/02/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Participation Weeks 1 - 3",
                  "category": "Minor Grades",
                  "dateAssigned": "10/17/2022",
                  "dateDue": "11/04/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "SCI43120A - 1    Aquatics S1",
              "grade": "93.50",
              "lastUpdated": "12/22/2022",
              "assignments": [
                {
                  "name": "Historical Oceanographers",
                  "category": "Minor Grades",
                  "dateAssigned": "12/16/2022",
                  "dateDue": "12/22/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Estuaries Assessment",
                  "category": "Minor Grades",
                  "dateAssigned": "12/13/2022",
                  "dateDue": "12/13/2022",
                  "score": "93.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Bays in Peril/Conservation of Texas Estuaries",
                  "category": "Non-graded",
                  "dateAssigned": "12/09/2022",
                  "dateDue": "12/13/2022",
                  "score": "L",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Estuaries Research Analysis",
                  "category": "Minor Grades",
                  "dateAssigned": "12/05/2022",
                  "dateDue": "12/05/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Estuaries Research",
                  "category": "Non-graded",
                  "dateAssigned": "12/01/2022",
                  "dateDue": "12/05/2022",
                  "score": "CNS",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Freshwater Assessment",
                  "category": "Minor Grades",
                  "dateAssigned": "11/17/2022",
                  "dateDue": "11/17/2022",
                  "score": "91.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Dragon Fly Pond Map",
                  "category": "Non-graded",
                  "dateAssigned": "11/09/2022",
                  "dateDue": "11/11/2022",
                  "score": "CNS",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Dragon Fly Pond",
                  "category": "Minor Grades",
                  "dateAssigned": "11/01/2022",
                  "dateDue": "11/07/2022",
                  "score": "90.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Environmental Concerns - Lakes and Streams",
                  "category": "Minor Grades",
                  "dateAssigned": "10/28/2022",
                  "dateDue": "11/01/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Lakes and Ponds",
                  "category": "Minor Grades",
                  "dateAssigned": "10/26/2022",
                  "dateDue": "11/01/2022",
                  "score": "94.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Watershed Lab",
                  "category": "Non-graded",
                  "dateAssigned": "10/18/2022",
                  "dateDue": "10/24/2022",
                  "score": "CNS",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Rivers",
                  "category": "Minor Grades",
                  "dateAssigned": "10/20/2022",
                  "dateDue": "10/20/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "SST23400A - 1    African American Studies S1",
              "grade": "100.00",
              "lastUpdated": "12/22/2022",
              "assignments": [
                {
                  "name": "Connect, Extend, Challenge: Economic Mobility",
                  "category": "Minor Grades",
                  "dateAssigned": "12/14/2022",
                  "dateDue": "12/14/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Intersectionality's Reflection",
                  "category": "Minor Grades",
                  "dateAssigned": "12/07/2022",
                  "dateDue": "12/07/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Case Studies over Court Cases",
                  "category": "Minor Grades",
                  "dateAssigned": "11/08/2022",
                  "dateDue": "11/14/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "African American Superhero",
                  "category": "Minor Grades",
                  "dateAssigned": "11/01/2022",
                  "dateDue": "11/08/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Black Wall Street Website Project",
                  "category": "Minor Grades",
                  "dateAssigned": "10/17/2022",
                  "dateDue": "10/25/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Journal Response Check",
                  "category": "Minor Grades",
                  "dateAssigned": "10/21/2022",
                  "dateDue": "10/21/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "SST71000A - 2    GT Amer Studies/AP US Hist S1",
              "grade": "",
              "lastUpdated": "",
              "assignments": []
            }
          ]
        }`
    },
    {
        type: "GET",
        id: "pastclasses",
        title: "Student Past Classes",
        description: "Get information on each class a student is taking including assignments and grades by quarter",
        queryParameters: [
            {
                title: "username",
                type: "string",
                description: "HAC Username",
                required: true
            },
            {
                title: "password",
                type: "string",
                description: "HAC Password",
                required: true
            },
            {
                title: "quarter",
                type: "number",
                description: "Grading quarter (1st, 2nd, 3rd, 4th)",
                required: true
            }
        ],
        exampleRequest: `axios.get("https://friscoisdhacapi.vercel.app/api/pastclasses?username=john&password=doe&quarter=1").then((res) => {
            console.log(res.data);
        }).catch((error) => {
            console.log(error);
        })`,
        exampleResponse: `
        {
          "pastClasses": [
            {
              "name": "CATE36300A - 1    Prac News Prod 1 S1",
              "grade": "93.33",
              "lastUpdated": "(Last+Updated: 12/20/2022",
              "assignments": [
                {
                  "name": "PA Script #4",
                  "category": "Minor Grades",
                  "dateAssigned": "10/03/2022",
                  "dateDue": "10/14/2022",
                  "score": "X",
                  "totalPoints": "100.00"
                },
                {
                  "name": "MP1 Package/Segment #2",
                  "category": "Minor Grades",
                  "dateAssigned": "09/12/2022",
                  "dateDue": "10/06/2022",
                  "score": "CNS",
                  "totalPoints": "100.00"
                },
                {
                  "name": "PA Script #3",
                  "category": "Minor Grades",
                  "dateAssigned": "09/12/2022",
                  "dateDue": "09/30/2022",
                  "score": "CNS",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Show Credits Practice",
                  "category": "Non-graded",
                  "dateAssigned": "09/12/2022",
                  "dateDue": "09/14/2022",
                  "score": "L",
                  "totalPoints": "100.00"
                },
                {
                  "name": "MP1 Package/Segment #1",
                  "category": "Minor Grades",
                  "dateAssigned": "08/10/2022",
                  "dateDue": "09/09/2022",
                  "score": "94.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "PA Script #2",
                  "category": "Minor Grades",
                  "dateAssigned": "08/26/2022",
                  "dateDue": "09/09/2022",
                  "score": "96.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "PA Script #1",
                  "category": "Minor Grades",
                  "dateAssigned": "08/10/2022",
                  "dateDue": "08/26/2022",
                  "score": "90.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Social Media Rollout",
                  "category": "Non-graded",
                  "dateAssigned": "08/10/2022",
                  "dateDue": "08/15/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "MP1 Calendar Check",
                  "category": "Non-graded",
                  "dateAssigned": "08/10/2022",
                  "dateDue": "08/10/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "ELA71000A - 2    GT Amer Studies/AP Lang S1",
              "grade": "87.20",
              "lastUpdated": "(Last+Updated: 12/20/2022",
              "assignments": [
                {
                  "name": "Ch. 19 Grade",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/03/2022",
                  "score": "50.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 18 Grade",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/27/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 17 Grade",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/20/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 16 Grade",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/13/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Reconstruction DBQ",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/07/2022",
                  "score": "85.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 15 Grade",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/07/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 14 Grade",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/30/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 14 Reading Questions",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/30/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 14 Quiz",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/30/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Civil War LEQ",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/25/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Lang Argument Essay #1",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/24/2022",
                  "score": "85.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Ch. 13 Reading Quiz",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/22/2022",
                  "score": "92.00",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "MTH34200A - 9    Pre Calculus Adv S1",
              "grade": "81.52",
              "lastUpdated": "(Last+Updated: 12/21/2022",
              "assignments": [
                {
                  "name": "Unit 2 Retest Eligibility (Yes=100, No=0)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "10/03/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 2 Delta Math Assignments (2.6, 2.7, 7.3)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/03/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 2 Test (Inequalities & PFD)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/03/2022",
                  "score": "85.31",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 2 Test (Rational Graphing)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "10/03/2022",
                  "score": "85.67",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 2 Review (Partiipation, NonGraded)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "09/30/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 2 Skill Check (Polynomial & Rational Inequalities)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/27/2022",
                  "score": "35.00",
                  "totalPoints": "50.00"
                },
                {
                  "name": "Unit 2 Quiz (Rational Graphing)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/21/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 1 Retest Eligibility (Yes=100, No=0)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "09/13/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 1 Delta Math (2.2, 2.3, 2.4-2.5)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/13/2022",
                  "score": "78.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 1 Test (2.4/2.5: Complex Numbers & Zeros of Polynomials)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/13/2022",
                  "score": "30.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 1 Test (2.2/2.3: Graphing & Dividing Polynomials)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/13/2022",
                  "score": "90.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 1 Review (Participation, NonGraded)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "09/09/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 1 Quiz (2.2/2.3 Graphing & Dividing Polynomials)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "09/07/2022",
                  "score": "90.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Factoring & Quadratic Formula Delta Math (NonGraded, Participation)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "08/26/2022",
                  "score": "0.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 0 Test 1.5/1.6 (Composition & Inverses)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/24/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 0 Test 1.3 (Even/Odd Functions & Transformations)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/24/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 0 Review Activity (NonGraded, Participation)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "08/23/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Unit 0 Delta Math",
                  "category": "Minor Grades",
                  "dateAssigned": "08/12/2022",
                  "dateDue": "08/23/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "1.5/1.6 Skill Check (Composition & Inverse Functions)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/23/2022",
                  "score": "35.00",
                  "totalPoints": "50.00"
                },
                {
                  "name": "1.3 Skill Check (Even/Odd Functions, Transformations)",
                  "category": "Minor Grades",
                  "dateAssigned": "",
                  "dateDue": "08/17/2022",
                  "score": "50.00",
                  "totalPoints": "50.00"
                },
                {
                  "name": "Get to Know You Form (NonGraded, Completion)",
                  "category": "Non-graded",
                  "dateAssigned": "",
                  "dateDue": "08/11/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "PEC03001A - 1    Cheerleading EQ3 S1",
              "grade": "100.00",
              "lastUpdated": "(Last+Updated: 12/21/2022",
              "assignments": [
                {
                  "name": "Weeks 7 - 9",
                  "category": "Minor Grades",
                  "dateAssigned": "09/26/2022",
                  "dateDue": "10/14/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Weeks 4 - 6",
                  "category": "Minor Grades",
                  "dateAssigned": "09/06/2022",
                  "dateDue": "09/23/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Weeks 1 - 3",
                  "category": "Minor Grades",
                  "dateAssigned": "08/10/2022",
                  "dateDue": "09/01/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "SCI43120A - 1    Aquatics S1",
              "grade": "95.00",
              "lastUpdated": "(Last+Updated: 12/22/2022",
              "assignments": [
                {
                  "name": "Freshwater Systems - Presentation",
                  "category": "Non-graded",
                  "dateAssigned": "09/28/2022",
                  "dateDue": "10/04/2022",
                  "score": "CNS",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Freshwater Systems - Information",
                  "category": "Minor Grades",
                  "dateAssigned": "09/28/2022",
                  "dateDue": "10/04/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Aquarium Chemistry and Set up",
                  "category": "Minor Grades",
                  "dateAssigned": "09/21/2022",
                  "dateDue": "09/21/2022",
                  "score": "80.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Aquarium Design",
                  "category": "Non-graded",
                  "dateAssigned": "09/08/2022",
                  "dateDue": "09/12/2022",
                  "score": "L",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Nutrient Cycles Explanation",
                  "category": "Minor Grades",
                  "dateAssigned": "08/30/2022",
                  "dateDue": "09/01/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Properties of Water",
                  "category": "Non-graded",
                  "dateAssigned": "08/23/2022",
                  "dateDue": "08/30/2022",
                  "score": "CNS",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Buoyancy and Density Practice",
                  "category": "Non-graded",
                  "dateAssigned": "08/22/2022",
                  "dateDue": "08/22/2022",
                  "score": "CNS",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Lab Safety Quiz",
                  "category": "Minor Grades",
                  "dateAssigned": "08/16/2022",
                  "dateDue": "08/16/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "SST23400A - 1    African American Studies S1",
              "grade": "98.33",
              "lastUpdated": "(Last+Updated: 12/22/2022",
              "assignments": [
                {
                  "name": "Connect, Extend, Challenge 13th 14th 15th Amendment",
                  "category": "Minor Grades",
                  "dateAssigned": "10/06/2022",
                  "dateDue": "10/06/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Jim Crow Era One Pager",
                  "category": "Minor Grades",
                  "dateAssigned": "10/04/2022",
                  "dateDue": "10/04/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Tenant/Sharecropping Farmers Podcast Episode",
                  "category": "Minor Grades",
                  "dateAssigned": "09/29/2022",
                  "dateDue": "09/29/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "African Civilizations Inquiry",
                  "category": "Minor Grades",
                  "dateAssigned": "09/06/2022",
                  "dateDue": "09/13/2022",
                  "score": "90.00",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Essential Question",
                  "category": "Minor Grades",
                  "dateAssigned": "09/09/2022",
                  "dateDue": "09/09/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                },
                {
                  "name": "Mini Current Event",
                  "category": "Minor Grades",
                  "dateAssigned": "08/17/2022",
                  "dateDue": "08/23/2022",
                  "score": "100.0",
                  "totalPoints": "100.00"
                }
              ]
            },
            {
              "name": "SST71000A - 2    GT Amer Studies/AP US Hist S1",
              "grade": "",
              "lastUpdated": "",
              "assignments": []
            }
          ]
        }`
    }
]

export default APIRoutes;