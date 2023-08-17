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
    description: "Get a student's most recently published GPAs and rank",
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
"weightedGPA" : "5.0500",
"rank" : "34 / 449"
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
    exampleResponse: `{
      "studentSchedule": [
        {
          "building": "Heritage High School",
          "courseCode": "ELA14300A - 1",
          "courseName": "AP English Literature S1",
          "days": "A",
          "markingPeriods": "Q1, Q2",
          "periods": "1",
          "room": "B106",
          "status": "Active",
          "teacher": "MATTSON, APRIL"
        },
        {
          "building": "Heritage High School",
          "courseCode": "SST34310 - 5",
          "courseName": "AP Economics",
          "days": "B",
          "markingPeriods": "Q1, Q2",
          "periods": "1",
          "room": "C117",
          "status": "Active",
          "teacher": "DEMPSEY, PATRICIA"
        },
        {
          "building": "Heritage High School",
          "courseCode": "ELA14300B - 1",
          "courseName": "AP English Literature S2",
          "days": "A",
          "markingPeriods": "Q3, Q4",
          "periods": "1",
          "room": "B106",
          "status": "Active",
          "teacher": "MATTSON, APRIL"
        },
        {
          "building": "Heritage High School",
          "courseCode": "SST34300 - 6",
          "courseName": "AP Government",
          "days": "B",
          "markingPeriods": "Q3, Q4",
          "periods": "1",
          "room": "C116",
          "status": "Active",
          "teacher": "Huggins, Jonathan"
        },
        {
          "building": "Heritage High School",
          "courseCode": "SCI43100A - 2",
          "courseName": "Environmental Systems S1",
          "days": "A",
          "markingPeriods": "Q1, Q2",
          "periods": "2",
          "room": "B204",
          "status": "Active",
          "teacher": "HART, MATT"
        },
        {
          "building": "Heritage High School",
          "courseCode": "PEC04001A - 1",
          "courseName": "Cheerleading EQ4 S1",
          "days": "B",
          "markingPeriods": "Q1, Q2",
          "periods": "2",
          "room": "G100",
          "status": "Active",
          "teacher": "Hollowell, Jacqueline"
        },
        {
          "building": "Heritage High School",
          "courseCode": "SCI43100B - 2",
          "courseName": "Environmental Systems S2",
          "days": "A",
          "markingPeriods": "Q3, Q4",
          "periods": "2",
          "room": "B204",
          "status": "Active",
          "teacher": "HART, MATT"
        },
        {
          "building": "Heritage High School",
          "courseCode": "PEC04001B - 1",
          "courseName": "Cheerleading EQ4 S2",
          "days": "B",
          "markingPeriods": "Q3, Q4",
          "periods": "2",
          "room": "G100",
          "status": "Active",
          "teacher": "Hollowell, Jacqueline"
        },
        {
          "building": "Heritage High School",
          "courseCode": "CATE36400A - 1",
          "courseName": "Pract News Prod 2 S1",
          "days": "A",
          "markingPeriods": "Q1, Q2",
          "periods": "3",
          "room": "A123",
          "status": "Active",
          "teacher": "BAGWELL, CANDACE"
        },
        {
          "building": "Heritage High School",
          "courseCode": "ELA43601A - 1",
          "courseName": "Ind Study Journalism 1 S1",
          "days": "B",
          "markingPeriods": "Q1, Q2",
          "periods": "3",
          "room": "A123",
          "status": "Active",
          "teacher": "BAGWELL, CANDACE"
        },
        {
          "building": "Heritage High School",
          "courseCode": "CATE36400B - 1",
          "courseName": "Pract News Prod 2 S2",
          "days": "A",
          "markingPeriods": "Q3, Q4",
          "periods": "3",
          "room": "A123",
          "status": "Active",
          "teacher": "BAGWELL, CANDACE"
        },
        {
          "building": "Heritage High School",
          "courseCode": "ELA43601B - 1",
          "courseName": "Ind Study Journalism 1 S2",
          "days": "B",
          "markingPeriods": "Q3, Q4",
          "periods": "3",
          "room": "A123",
          "status": "Active",
          "teacher": "BAGWELL, CANDACE"
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
          "courseCode": "REL99013A - 2",
          "courseName": "Rel 4A OR 4B S1",
          "days": "B",
          "markingPeriods": "Q1, Q2",
          "periods": "4",
          "room": "N/A",
          "status": "Active",
          "teacher": "Staff"
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
          "courseCode": "REL99013B - 2",
          "courseName": "Rel 4A OR 4B S2",
          "days": "B",
          "markingPeriods": "Q3, Q4",
          "periods": "4",
          "room": "N/A",
          "status": "Active",
          "teacher": "Staff"
        },
        {
          "building": "Heritage High School",
          "courseCode": "MSC15133M - 47",
          "courseName": "Advisory Estel/Ward (Pack)",
          "days": "A, B",
          "markingPeriods": "Q1, Q2, Q3, Q4",
          "periods": "ADV",
          "room": "G117",
          "status": "Active",
          "teacher": "ESTEL, SYDNE"
        }
      ]
    }`
  },
  {
    type: "GET",
    id: "transcript",
    title: "Student Transcript",
    description: "Get a student's transcript",
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
    exampleRequest: `/api/transcript?username=john&password=doe`,
    exampleResponse: `{
      "studentTranscript": [
        {
          "yearsAttended": "2019-2020",
          "gradeLevel": "08",
          "building": "Maus Middle School",
          "totalCredits": "0.5000",
          "courses": [
            {
              "courseCode": "03810100 - 1",
              "courseName": "HLTH ED",
              "sem1Grade": "100",
              "sem2Grade": "",
              "finalGrade": "",
              "courseCredits": "0.5000"
            }
          ]
        },
        {
          "yearsAttended": "2020-2021",
          "gradeLevel": "09",
          "building": "Heritage High School",
          "totalCredits": "8.0000",
          "courses": [
            {
              "courseCode": "03320100 - 1",
              "courseName": "W GEO",
              "sem1Grade": "",
              "sem2Grade": "92",
              "finalGrade": "",
              "courseCredits": "0.5000"
            },
            {
              "courseCode": "03580510 - 1",
              "courseName": "TA3DMA",
              "sem1Grade": "97",
              "sem2Grade": "66",
              "finalGrade": "82",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03220100 - 1",
              "courseName": "ENG 1",
              "sem1Grade": "70",
              "sem2Grade": "87",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03440100 - 1",
              "courseName": "SPAN 1",
              "sem1Grade": "93",
              "sem2Grade": "90",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "A3360100 - 1",
              "courseName": "APHUMGEOW",
              "sem1Grade": "72",
              "sem2Grade": "66",
              "finalGrade": "",
              "courseCredits": "0.5000"
            },
            {
              "courseCode": "03230800 - 1",
              "courseName": "PHOTJOUR",
              "sem1Grade": "85",
              "sem2Grade": "83",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03231900 - 1",
              "courseName": "BRCTJOR1",
              "sem1Grade": "86",
              "sem2Grade": "89",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03010200 - 1",
              "courseName": "BIO",
              "sem1Grade": "74",
              "sem2Grade": "88",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03100500 - 1",
              "courseName": "ALG 1",
              "sem1Grade": "75",
              "sem2Grade": "80",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "waivertech - 1",
              "courseName": "Tech Waiver",
              "sem1Grade": "W",
              "sem2Grade": "",
              "finalGrade": "",
              "courseCredits": "0.0000"
            },
            {
              "courseCode": "waivertech - 2",
              "courseName": "Tech Waiver",
              "sem1Grade": "",
              "sem2Grade": "W",
              "finalGrade": "",
              "courseCredits": "0.0000"
            }
          ]
        },
        {
          "yearsAttended": "2021-2022",
          "gradeLevel": "10",
          "building": "Heritage High School",
          "totalCredits": "9.0000",
          "courses": [
            {
              "courseCode": "03100600 - 1",
              "courseName": "ALG 2",
              "sem1Grade": "83",
              "sem2Grade": "88",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03100700 - 1",
              "courseName": "GEOM",
              "sem1Grade": "82",
              "sem2Grade": "95",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03220200 - 1",
              "courseName": "ENG 2",
              "sem1Grade": "98",
              "sem2Grade": "94",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03500100 - 1",
              "courseName": "ART 1",
              "sem1Grade": "100",
              "sem2Grade": "100",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03040000 - 1",
              "courseName": "CHEM",
              "sem1Grade": "92",
              "sem2Grade": "90",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03440200 - 1",
              "courseName": "SPAN 2",
              "sem1Grade": "97",
              "sem2Grade": "93",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03240600 - 1",
              "courseName": "DEBATE 1",
              "sem1Grade": "100",
              "sem2Grade": "100",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "A3370100 - 1",
              "courseName": "APWHIST",
              "sem1Grade": "89",
              "sem2Grade": "90",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "13008600 - 1",
              "courseName": "AVPROD2",
              "sem1Grade": "88",
              "sem2Grade": "96",
              "finalGrade": "",
              "courseCredits": "1.0000"
            }
          ]
        },
        {
          "yearsAttended": "2022-2023",
          "gradeLevel": "11",
          "building": "Heritage High School",
          "totalCredits": "8.0000",
          "courses": [
            {
              "courseCode": "A3340100 - 1",
              "courseName": "APUSHIST",
              "sem1Grade": "90",
              "sem2Grade": "81",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03380085 - 1",
              "courseName": "AFAMSTUD",
              "sem1Grade": "99",
              "sem2Grade": "99",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "A3220100 - 1",
              "courseName": "APENGLAN",
              "sem1Grade": "90",
              "sem2Grade": "81",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03030000 - 1",
              "courseName": "AQUA SCI",
              "sem1Grade": "95",
              "sem2Grade": "93",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "03101100 - 1",
              "courseName": "PRE CALC",
              "sem1Grade": "83",
              "sem2Grade": "85",
              "finalGrade": "",
              "courseCredits": "1.0000"
            },
            {
              "courseCode": "13008700 - 1",
              "courseName": "PRACAVP1",
              "sem1Grade": "92",
              "sem2Grade": "91",
              "finalGrade": "",
              "courseCredits": "2.0000"
            },
            {
              "courseCode": "PES00002 - 1",
              "courseName": "SUBATH3",
              "sem1Grade": "100",
              "sem2Grade": "100",
              "finalGrade": "",
              "courseCredits": "1.0000"
            }
          ]
        }
      ]
    }`
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
    exampleResponse: `{
      "currentClasses": [
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
    exampleRequest: "/api/pastclasses?username=john&password=doe&quarter=1",
    exampleResponse: `{
      "pastClasses": [
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
      ]
    }`
  }
]

export default APIRoutes;