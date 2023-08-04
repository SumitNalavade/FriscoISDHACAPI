import IAPIRoute from "./apiRouteInterface";

const APIRoutes: IAPIRoute[] = [
    {
        type: "GET",
        id: "info",
        title: "Student Info",
        description: "Get a student's personal information",
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
        exampleRequest: `/api/info?username=john&password=doe`,
        exampleResponse: `{
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
        description: "Get a student's most recently published GPAs and total number of credits taken",
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
        exampleRequest: `/api/gpa?username=john&password=doe`,
        exampleResponse: `{
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
        exampleRequest: `/api/schedule?username=john&password=doe`,
        exampleResponse: `[
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
]`
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
        exampleRequest: `/api/currentclasses?username=john&password=doe`,
        exampleResponse: `[
  {
    "name": "CATE27600B - 3    Mobile App Programming S2@CTEC",
    "grade": "",
    "weight": "6",
    "credits": "1",
    "lastUpdated": "",
    "assignments": []
  },

  {
    "name": "CATE36400B - 1    Prac News Prod 2 S2",
    "grade": "",
    "weight": "5",
    "credits": "1",
    "lastUpdated": "1/6/2022",
    "assignments": [
      {
        "name": "PA Script #3",
        "category": "Minor Grades",
        "dateAssigned": "02/09/2022",
        "dateDue": "03/04/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Social Media Posts",
        "category": "Minor Grades",
        "dateAssigned": "01/04/2022",
        "dateDue": "03/02/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "MP3 Package/Segment #2",
        "category": "Major Grades",
        "dateAssigned": "01/10/2022",
        "dateDue": "03/02/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Event Coverage",
        "category": "Major Grades",
        "dateAssigned": "01/04/2022",
        "dateDue": "02/25/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "PA Script #2",
        "category": "Minor Grades",
        "dateAssigned": "01/24/2022",
        "dateDue": "02/08/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "MP3 Package/Segment #1",
        "category": "Major Grades",
        "dateAssigned": "01/11/2022",
        "dateDue": "02/04/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "PA Script #1",
        "category": "Minor Grades",
        "dateAssigned": "01/04/2022",
        "dateDue": "01/21/2022",
        "score": "97.00",
        "totalPoints": "100.00"
      },
      {
        "name": "MP3 Calendar Check",
        "category": "Non-graded",
        "dateAssigned": "01/04/2022",
        "dateDue": "01/06/2022",
        "score": "100.0",
        "totalPoints": "100.00"
      }
    ]
  },

  {
    "name": "ELA14300B - 4    AP English Literature S2",
    "grade": "85.00",
    "weight": "6",
    "credits": "1",
    "lastUpdated": "1/13/2022",
    "assignments": [
      {
        "name": "Thesis Practice #1",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/13/2022",
        "score": "90.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Christmas Carol Q3 Essay",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/05/2022",
        "score": "80.00",
        "totalPoints": "100.00"
      }
    ]
  },

  {
    "name": "MTH45300B - 1    AP Calculus AB S2",
    "grade": "80.80",
    "weight": "6",
    "credits": "1",
    "lastUpdated": "1/10/2022",
    "assignments": [
      {
        "name": "Unit 6 Test (Integration)",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "02/08/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Delta Math Practice (Unit 6)",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "02/08/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Quiz 4 (Antiderivatives and Rules of Integration)",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/31/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Quiz 3 (FTC and Definite Integrals)",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/27/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Quiz 2 (Properties of Def. Integrals)",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/25/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Quiz 1 (Reimann Sums and Definite Integrals)",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/19/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 5 Test (Analytical Applications of Derivatives)",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "01/10/2022",
        "score": "78.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Delta Math Practice (Unit 5)",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/10/2022",
        "score": "85.00",
        "totalPoints": "100.00"
      }
    ]
  },

  {
    "name": "MTH45310B - 4    AP Statistics S2",
    "grade": "0.00",
    "weight": "6",
    "credits": "1",
    "lastUpdated": "",
    "assignments": [
      {
        "name": "Test - 8 Confidence Intervals",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "01/26/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Skills Check - 8 Confidence Intervals",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/24/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Practice - 8.3 (canvas)",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "01/24/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Practice - 8.2 (canvas)",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "01/24/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Practice - 8.1 (canvas)",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "01/24/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Group Skills Check - 7 Sampling Distributions",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/11/2022",
        "score": "",
        "totalPoints": "50.00"
      }
    ]
  },

  {
    "name": "SCI43300B - 1    AP Environmental Science S2",
    "grade": "",
    "weight": "6",
    "credits": "1",
    "lastUpdated": "",
    "assignments": []
  },

  {
    "name": "SST34300 - 4    AP Government",
    "grade": "0.00",
    "weight": "6",
    "credits": "1",
    "lastUpdated": "",
    "assignments": [
      {
        "name": "Midterm Exam (Units 1 & 2)",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "02/23/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 2 Major Grade FRQ",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "02/16/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 2 MC Quiz",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "02/14/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 2 Argument FRQ Practice",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "02/11/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 2 Congress FRQ Practice",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "02/04/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 Major Grade FRQ",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "01/21/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 MC Quiz",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/21/2022",
        "score": "",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 Concept Application & Argument FRQ Practice",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "01/14/2022",
        "score": "",
        "totalPoints": "100.00"
      }
    ]
  }
]`
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
        exampleRequest: "/api/pastclasses?username=john&password=doe&quarter=1",
        exampleResponse: `[
  {
    "lastUpdated": "12/17/2021",
    "assignments": [
      {
        "name": "Loops and lists",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "10/12/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Loops",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "10/04/2021",
        "score": "CWS",
        "totalPoints": "100.00"
      },
      {
        "name": "Collections",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/30/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Classes and structures",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "08/27/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Programmatically creating UI components",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/27/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Creating simple UI components",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/27/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Introductory Swift",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/19/2021",
        "score": "CWS",
        "totalPoints": "100.00"
      },
      {
        "name": "App dev cycle",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/17/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      }
    ],
    "credits": "1",
    "grade": "100.00",
    "name": "CATE27600A - 3    Mobile App Programming S1@CTEC",
    "weight": "6"
  },
  {
    "lastUpdated": "12/26/2021",
    "assignments": [
      {
        "name": "MP2 Package/Segment",
        "category": "Major Grades",
        "dateAssigned": "09/27/2021",
        "dateDue": "10/15/2021",
        "score": "83.00",
        "totalPoints": "100.00"
      },
      {
        "name": "PA Script #4",
        "category": "Minor Grades",
        "dateAssigned": "09/24/2021",
        "dateDue": "10/15/2021",
        "score": "95.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Show Elements (Show Open, Graphics, etc)",
        "category": "Minor Grades",
        "dateAssigned": "08/16/2021",
        "dateDue": "10/15/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Social Media Post #2",
        "category": "Minor Grades",
        "dateAssigned": "09/27/2021",
        "dateDue": "10/15/2021",
        "score": "91.00",
        "totalPoints": "100.00"
      },
      {
        "name": "PA Script #3",
        "category": "Minor Grades",
        "dateAssigned": "09/20/2021",
        "dateDue": "10/15/2021",
        "score": "89.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Event Coverage",
        "category": "Major Grades",
        "dateAssigned": "08/12/2021",
        "dateDue": "10/07/2021",
        "score": "60.00",
        "totalPoints": "100.00"
      },
      {
        "name": "MP1 Package/Segment #1",
        "category": "Major Grades",
        "dateAssigned": "08/16/2021",
        "dateDue": "09/24/2021",
        "score": "97.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Social Media Post #1",
        "category": "Minor Grades",
        "dateAssigned": "08/24/2021",
        "dateDue": "09/24/2021",
        "score": "98.00",
        "totalPoints": "100.00"
      },
      {
        "name": "PA Script #2",
        "category": "Minor Grades",
        "dateAssigned": "09/01/2021",
        "dateDue": "09/17/2021",
        "score": "93.00",
        "totalPoints": "100.00"
      },
      {
        "name": "PA Script #1",
        "category": "Minor Grades",
        "dateAssigned": "08/12/2021",
        "dateDue": "08/31/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Practicum Training Plan",
        "category": "Minor Grades",
        "dateAssigned": "08/12/2021",
        "dateDue": "08/26/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "MP1 Calendar Check",
        "category": "Non-graded",
        "dateAssigned": "08/12/2021",
        "dateDue": "08/16/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      }
    ],
    "credits": "1",
    "grade": "86.30",
    "name": "CATE36400A - 1    Prac News Prod 2 S1",
    "weight": "5"
  },
  {
    "lastUpdated": "12/17/2021",
    "assignments": [
      {
        "name": "Timed Write #2",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "10/05/2021",
        "score": "85.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Macbeth Soliloquy",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "10/04/2021",
        "score": "85.00",
        "totalPoints": "100.00"
      },
      {
        "name": "College Essay",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/17/2021",
        "score": "85.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Macbeth Quiz",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/14/2021",
        "score": "92.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Macbeth Timed Writing",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/01/2021",
        "score": "80.00",
        "totalPoints": "100.00"
      },
      {
        "name": "College Essay OUTLINE, 10C",
        "category": "Minor Grades",
        "dateAssigned": "08/27/2021",
        "dateDue": "08/27/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Macbeth Pre-Reading Questions, 4F",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/20/2021",
        "score": "80.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Intro Letter, 9E",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/12/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      }
    ],
    "credits": "1",
    "grade": "86.80",
    "name": "ELA14300A - 4    AP English Literature S1",
    "weight": "6"
  },
  {
    "lastUpdated": "12/8/2021",
    "assignments": [
      {
        "name": "Unit 2 Test (Limit Def'n of Deriv, Basic Derivative Rules)",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "10/07/2021",
        "score": "85.00",
        "totalPoints": "100.00"
      },
      {
        "name": "2.4,2.6 Delta Math Practice",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "10/05/2021",
        "score": "94.00",
        "totalPoints": "100.00"
      },
      {
        "name": "2.3,2.5 Delta Math Practice",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/24/2021",
        "score": "96.00",
        "totalPoints": "100.00"
      },
      {
        "name": "2.1-2.2 Delta Math Practice",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/20/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 Test (Limits)",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/09/2021",
        "score": "83.00",
        "totalPoints": "100.00"
      },
      {
        "name": "1.7-1.8 Delta Math Average",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/01/2021",
        "score": "90.00",
        "totalPoints": "100.00"
      },
      {
        "name": "1.4-1.6 Delta Math Practice",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/30/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "1.1-1.3 Delta Math Average",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/20/2021",
        "score": "89.00",
        "totalPoints": "100.00"
      },
      {
        "name": "1.2 Skills Check (Limits Graphically)",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/16/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      }
    ],
    "credits": "1",
    "grade": "88.63",
    "name": "MTH45300A - 1    AP Calculus AB S1",
    "weight": "6"
  },
  {
    "lastUpdated": "12/17/2021",
    "assignments": [
      {
        "name": "Test - 3.2 Least Squares Regression",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "10/07/2021",
        "score": "71.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Test - 3.1 Scatterplots and Correlation",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "10/07/2021",
        "score": "71.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Review - 3 Describing Relationships",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "10/07/2021",
        "score": "58.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Skills Check - 3.2 LSRL, Residuals, and Residual Plots",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "10/04/2021",
        "score": "89.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Skills Check - 3.1 Scatterplots and Correlation",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/30/2021",
        "score": "79.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Test - 2.2 Normal Distributions",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/24/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Test - 2.1 Describing Location",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/24/2021",
        "score": "92.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Review - 2 Modeling Distributions of Data",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/24/2021",
        "score": "91.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Skills Check - 2.2 Density Curves and Normal Distributions",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/20/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Practice - 2.2 Normal Distributions",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/20/2021",
        "score": "L",
        "totalPoints": "100.00"
      },
      {
        "name": "Practice - 2.2 Density Curves and the Empirical Rule",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/20/2021",
        "score": "60.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Skills Check - 2.1 Describing Location",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/16/2021",
        "score": "92.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Practice - 2.1",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/16/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Test - 1 Exploring Data",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/08/2021",
        "score": "89.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Quiz - 1 Exploring Data",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/02/2021",
        "score": "89.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Skills Check - 1.1 Analyzing Categorical Data",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/23/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      }
    ],
    "credits": "1",
    "grade": "87.37",
    "name": "MTH45310A - 4    AP Statistics S1",
    "weight": "6"
  },
  {
    "lastUpdated": "12/17/2021",
    "assignments": [
      {
        "name": "Unit 2 Assessment - Biodiversity_all topics",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "10/13/2021",
        "score": "86.67",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 2 QUIZ - Topics 2.1-2.3",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "10/06/2021",
        "score": "86.67",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 2 - Island Biogeography Lab",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "10/04/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 - Ecosystem project",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/24/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 Assessment - all Topics",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/22/2021",
        "score": "91.67",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 - Topics 1.8-1.11 QUIZ",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/16/2021",
        "score": "93.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Owl Pellet Lab- Flow of Energy",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/16/2021",
        "score": "97.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 - Topics 1.4-1.7 QUIZ (BGC cycles)",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/02/2021",
        "score": "95.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Bozeman- BGC Cycles Performance Task",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/02/2021",
        "score": "96.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 - Topics 1.1 - 1.3 QUIZ",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/25/2021",
        "score": "91.67",
        "totalPoints": "100.00"
      }
    ],
    "credits": "1",
    "grade": "91.47",
    "name": "SCI43300A - 1    AP Environmental Science S1",
    "weight": "6"
  },
  {
    "lastUpdated": "12/10/2021",
    "assignments": [
      {
        "name": "Units 1-3 FRQ Test: Choice #2",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/27/2021",
        "score": "88.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Units 1-3 FRQ Test: Choice #1",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/27/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Units 1-3 FRQ Test: Required Question",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/27/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Units 1-3 MCQ Test: Unit 3 Topic",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/27/2021",
        "score": "94.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Units 1-3 MCQ Test: Unit 2 Topic",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/27/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Units 1-3 MCQ Test: Unit 1 Topic",
        "category": "Major Grades",
        "dateAssigned": "",
        "dateDue": "09/27/2021",
        "score": "79.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 3 FRQ Quiz",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/23/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 3 MCQ Quiz",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/23/2021",
        "score": "96.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 3 AP Classroom Progress Check MCQ",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/21/2021",
        "score": "INS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 3.5: Return to LRAS",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/17/2021",
        "score": "INS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 3.3: Fiscal Policy",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/15/2021",
        "score": "INS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 3.2: Potential Output and Gaps",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/13/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 3.1: AD/SRAS/LRAS",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/09/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 2 FRQ Quiz",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/09/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 2 MCQ Quiz",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "09/09/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 2 AP Classroom Progress Check MCQ",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/07/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 2.4: Business Cycle",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/01/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 2.3: Inflation",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "09/01/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 2.2: Unemployment",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "08/30/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 2.1: Circular Flow and GDP",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "08/26/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 FRQ Quiz",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/26/2021",
        "score": "100.0",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 MCQ Quiz",
        "category": "Minor Grades",
        "dateAssigned": "",
        "dateDue": "08/26/2021",
        "score": "88.00",
        "totalPoints": "100.00"
      },
      {
        "name": "Unit 1 AP Classroom Progress Check MCQ",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "08/24/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 1.4: Double Shifts & Disequilibrium",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "08/20/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 1.3: Micro Markets",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "08/18/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 1.2: Production Possibilities Curve",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "08/16/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      },
      {
        "name": "Flipped Video 1.1: Scarcity",
        "category": "Non-graded",
        "dateAssigned": "",
        "dateDue": "08/12/2021",
        "score": "CNS",
        "totalPoints": "100.00"
      }
    ],
    "credits": "1",
    "grade": "94.43",
    "name": "SST34310 - 3    AP Economics",
    "weight": "6"
  }
]`
    }
]

export default APIRoutes;