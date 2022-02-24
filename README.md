
# FRISCO ISD HAC API

REST API to scrape student information from Frisco ISD's Home Access Center (HAC) using python requests and Beautiful Soup


Powers the Gradual Grades mobile app developed with @mjdierkes. https://github.com/mjdierkes


----------

Base API URL: https://gradual-deploy.vercel.app

Technologies Used:
-
- Python
- Flask
- BeautifulSoup
- Vercel
- Heroku



## API Reference

**Demo Username: "John"**

**Demo Password: "Doe"**

Note: Make sure to pass username and password as query strings for GET routes

Routes:
- GET student GPAs
- GET student information
- GET student schedule
- GET student class data with assignment details
- POST get student predicted GPAs
- GET SAT testing dates

<br>

#### Get a students HAC weighted & unweighted GPA

```http
  GET /students/gpa/{username}/{password}
```
Query Parameters:
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. HAC username|
| `password` | `string` | **Required**. HAC password|

Example Request (Axios):
``` javascript
axios.get("https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe").then((res) => {
    console.log(res.data); //Make sure to denote what data you want from the response
}).catch((error) => {
    console.log(error);
})
```
cURL:
``` cURL
curl -X GET \
  'https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)'
```

Response:
``` json
{
    "unweightedGPA" : "3.8800",
    "weightedGPA" : "5.0500"
}
```

<br>

#### Get student information (Name, Grade, Counselor etc...)

```http
  GET /students/info/{username}/{password}
```
Query Parameters:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. HAC username|
| `password`      | `string` | **Required**. HAC password|

Example Request (Axios):
``` javascript
axios.get("https://gradual-deploy.vercel.app/students/info?username=john&password=doe").then((res) => {
    console.log(res.data);
}).catch((error) => {
    console.log(error);
})
```
cURL:
``` cURL
curl -X GET \
  'https://gradual-deploy.vercel.app/students/info?username=john&password=doe' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)'
```

Response:
``` json
{
    "studentBirthDate": "12/24/2003",
    "studentBuilding": "Heritage High School",
    "studentGrade": "12",
    "studentID": "123456",
    "studentName": "Jonh Doe"
}
```

<br>

#### Get student schedule

```http
  GET /students/schedule/{username}/{password}
```
Query Parameters:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. HAC username|
| `password`      | `string` | **Required**. HAC password|

Example Request (Axios):
``` javascript
axios.get("https://gradual-deploy.vercel.app/students/schedule?username=john&password=doe").then((res) => {
    console.log(res.data);
}).catch((error) => {
    console.log(error);
})
```
cURL:
``` cURL
curl -X GET \
  'https://gradual-deploy.vercel.app/students/schedule?username=john&password=doe' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)'
```

Response:
``` json
{
  "schedule": [
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
```

<br>

#### Get student's current classes information (Name, Grade, Weight, Credits) and assignments

```http
  GET /students/currentclasses/{username}/{password}
```
Query Parameters:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. HAC username |
| `password`      | `string` | **Required**. HAC password |

Example Request (Axios):
``` javascript
axios.get("https://gradual-deploy.vercel.app/students/currentclasses?username=john&password=doe").then((res) => {
    console.log(res.data);
}).catch((error) => {
    console.log(error);
})
```

``` cURL
curl -X GET \
  'https://gradual-deploy.vercel.app/students/currentclasses?username=john&password=doe' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)'
```

Response:
``` json
{
  "currentClasses": [
    {
      "name": "CATE27600B - 3    Mobile App Programming S2@CTEC",
      "grade": "",
      "weight": "6",
      "credits": "1"
      "Last Updated": "",
      "assignments": []
    },

    {
      "name": "CATE36400B - 1    Prac News Prod 2 S2",
      "grade": "",
      "weight": "5",
      "credits": "1",
      "Last Updated": "1/6/2022",
      "assignments": [
        {
          "assignment": "PA Script #3",
          "category": "Minor Grades",
          "dateAssigned": "02/09/2022",
          "dateDue": "03/04/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Social Media Posts",
          "category": "Minor Grades",
          "dateAssigned": "01/04/2022",
          "dateDue": "03/02/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "MP3 Package/Segment #2",
          "category": "Major Grades",
          "dateAssigned": "01/10/2022",
          "dateDue": "03/02/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Event Coverage",
          "category": "Major Grades",
          "dateAssigned": "01/04/2022",
          "dateDue": "02/25/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "PA Script #2",
          "category": "Minor Grades",
          "dateAssigned": "01/24/2022",
          "dateDue": "02/08/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "MP3 Package/Segment #1",
          "category": "Major Grades",
          "dateAssigned": "01/11/2022",
          "dateDue": "02/04/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "PA Script #1",
          "category": "Minor Grades",
          "dateAssigned": "01/04/2022",
          "dateDue": "01/21/2022",
          "score": "97.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "MP3 Calendar Check",
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
      "Last Updated": "1/13/2022",
      "assignments": [
        {
          "assignment": "Thesis Practice #1",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "01/13/2022",
          "score": "90.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Christmas Carol Q3 Essay",
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
      "Last Updated": "1/10/2022",
      "assignments": [
        {
          "assignment": "Unit 6 Test (Integration)",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "02/08/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Delta Math Practice (Unit 6)",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "02/08/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Quiz 4 (Antiderivatives and Rules of Integration)",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "01/31/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Quiz 3 (FTC and Definite Integrals)",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "01/27/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Quiz 2 (Properties of Def. Integrals)",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "01/25/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Quiz 1 (Reimann Sums and Definite Integrals)",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "01/19/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 5 Test (Analytical Applications of Derivatives)",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "01/10/2022",
          "score": "78.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Delta Math Practice (Unit 5)",
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
      "Last Updated": "",
      "assignments": [
        {
          "assignment": "Test - 8 Confidence Intervals",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "01/26/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Skills Check - 8 Confidence Intervals",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "01/24/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Practice - 8.3 (canvas)",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "01/24/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Practice - 8.2 (canvas)",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "01/24/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Practice - 8.1 (canvas)",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "01/24/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Group Skills Check - 7 Sampling Distributions",
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
      "Last Updated": "",
      "assignments": []
    },

    {
      "name": "SST34300 - 4    AP Government",
      "grade": "0.00",
      "weight": "6",
      "credits": "1",
      "Last Updated": "",
      "assignments": [
        {
          "assignment": "Midterm Exam (Units 1 & 2)",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "02/23/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 2 Major Grade FRQ",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "02/16/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 2 MC Quiz",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "02/14/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 2 Argument FRQ Practice",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "02/11/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 2 Congress FRQ Practice",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "02/04/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 Major Grade FRQ",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "01/21/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 MC Quiz",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "01/21/2022",
          "score": "",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 Concept Application & Argument FRQ Practice",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "01/14/2022",
          "score": "",
          "totalPoints": "100.00"
        }
      ]
    }

  ]
}
```

<br>

#### Get student's predicted GPAs

```http
  POST /predictedGPA
```
Body (JSON): *Route will accept only JSON data in the body

*All numbers must not be strings
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `weightedGPA` | `number` | **Required**. Student's weighted GPA in HAC |
| `unweightedGPA`| `number` | **Required**. Student's unweighted GPA in HAC |
| `studentGrade`| `number` | **Required**. Student's current grade level |
| `currentClasses`| `array` | **Required**. Array of student class objects (You can use /students/currentClasses to get this)|

Example Request (Axios):

```javascript
  axios.post(`https://gradual-deploy.vercel.app/predictedGPA`, {
    weightedGPA: 5.05,
    unweightedGPA: 3.88,
    studentGrade: 12,
    currentClasses: [
        {
          "name": "CATE27600A - 3    Mobile App Programming S1@CTEC",
          "grade": 100,
          "weight": 6,
          "credits": 1
        },
        {
          "name": "CATE36400A - 1    Prac News Prod 2 S1",
          "grade": 91.48,
          "weight": 5,
          "credits": 1
        },
        {
          "name": "ELA14300A - 4    AP English Literature S1",
          "grade": 88.13,
          "weight": 6,
          "credits": 1
        },
        {
          "name": "MTH45300A - 1    AP Calculus AB S1",
          "grade": 79.4,
          "weight": 6,
          "credits": 1
        },
        {
          "name": "MTH45310A - 4    AP Statistics S1",
          "grade": 79.48,
          "weight": 6,
          "credits": 1
        },
        {
          "name": "SCI43300A - 1    AP Environmental Science S1",
          "grade": 94,
          "weight": 6,
          "credits": 1
        },
        {
          "name": "SST34310 - 3    AP Economics",
          "grade": 93.24,
          "weight": 6,
          "credits": 1
        }
      ]
}).then((result) => {
    console.log(result.data);
}).catch((error) => {
    console.log(error);
})
```

Example Request (cURL):
``` cURL
curl -X POST \
  'https://gradual-deploy.vercel.app/predictedGPA' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)' \
  -H 'Content-Type: application/json' \
  -d '{
    "weightedGPA" : 5.05,
    "unweightedGPA" : 3.88,
    "studentGrade" : 12,
    "currentClasses" : [
  {
    "name": "CATE27600A - 3    Mobile App Programming S1@CTEC",
    "grade": 100,
    "weight": 6,
    "credits": 1
  },
  {
    "name": "CATE36400A - 1    Prac News Prod 2 S1",
    "grade": 91.48,
    "weight": 5,
    "credits": 1
  },
  {
    "name": "ELA14300A - 4    AP English Literature S1",
    "grade": 88.13,
    "weight": 6,
    "credits": 1
  },
  {
    "name": "MTH45300A - 1    AP Calculus AB S1",
    "grade": 79.4,
    "weight": 6,
    "credits": 1
  },
  {
    "name": "MTH45310A - 4    AP Statistics S1",
    "grade": 79.48,
    "weight": 6,
    "credits": 1
  },
  {
    "name": "SCI43300A - 1    AP Environmental Science S1",
    "grade": 94,
    "weight": 6,
    "credits": 1
  },
  {
    "name": "SST34310 - 3    AP Economics",
    "grade": 93.24,
    "weight": 6,
    "credits": 1
  }
]
}'
```

Response
``` json
{
  "finalWeightedGPA": "5.018267857142857",
  "finalUnweightedGPA": "3.8539464285714287"
}
```

<br>

#### Get upcoming SAT testing dates from CollegeBoard

```http
  GET /satdates
```

Example Request (Axios):
``` javascript
axios.get("https://gradual-deploy.vercel.app/satdates").then((res) => {
    console.log(res.data); //Make sure to denote what data you want from the response
}).catch((error) => {
    console.log(error);
})
```
cURL:
``` cURL
curl -X GET \
  'https://gradual-deploy.vercel.app/satdates' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)'
```

Response:
``` json
{
  "dates": [
    "Aug 28, 2021",
    "Oct 2, 2021",
    "Nov 6, 2021",
    "Dec 4, 2021",
    "Mar 12, 2022",
    "May 7, 2022",
    "Jun 4, 2022"
  ]
}
```

<br>
## FAQ

#### How secure is the API

No user information is stored in any databases. All of the proccessing that happens in a request is dumped once the request has resolved.

## Feedback

If you have any feedback, please reach out to me at vs.nalavade2003@gmail.com

## License

[Creative Commons ShareAlike 4.0]https://creativecommons.org/licenses/by-sa/4.0/

