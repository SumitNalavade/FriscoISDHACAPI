---
sidebar_position: 5
---

# [GET] Class Information By Quarter

Get information on each class a student is taking including assignments and grades by quarter

```http
GET /students/pastassignments?username={username}&password={password}&quarter={quarter}
```

### Query Parameters
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. HAC username|
| `password` | `string` | **Required**. HAC password|
| `quarter` | `string` | **Required**. Grading quarter (1st, 2nd, 3rd, 4th)|

### Example Requests

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs
  defaultValue="Node.js"
>
<TabItem value="Node.js" label="Node.js (Axios)">

```js
axios.get("https://gradual-deploy.vercel.app/students/pastassignments?username=john&password=doe&quarter=1").then((res) => {
    console.log(res.data);
}).catch((error) => {
    console.log(error);
})
```

</TabItem>
<TabItem value="Javascript (Fetch)">

```js
fetch("https://gradual-deploy.vercel.app/students/pastassignments?username=john&password=doe&quarter=1", { 
  method: "GET"
}).then(function(response) {
  return response.text();
}).then(function(data) {
  console.log(data);
})
```

</TabItem>
<TabItem value="Python">

```python
import requests

reqUrl = "https://gradual-deploy.vercel.app/students/pastassignments?username=john&password=doe&quarter=1"

payload = ""

response = requests.request("GET", reqUrl, data=payload)

print(response.text)
```

</TabItem>

<TabItem value="C#">

```cs
var client = new HttpClient();
var request = new HttpRequestMessage();
request.RequestUri = new Uri("https://gradual-deploy.vercel.app/students/pastassignments?username=john&password=doe&quarter=1");
request.Method = HttpMethod.Get;

request.Headers.Add("Accept", "*/*");
request.Headers.Add("User-Agent", "Thunder Client (https://www.thunderclient.com)");

var response = await client.SendAsync(request);
var result = await response.Content.ReadAsStringAsync();
Console.WriteLine(result);
```

</TabItem>

<TabItem value="cURL">

```cURL
curl -X GET \
  'https://gradual-deploy.vercel.app/students/pastassignments?username=john&password=doe&quarter=1' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)'
```

</TabItem>
</Tabs>

### Example Response
```json
  {
  "currentClasses": [
    {
      "Last Updated": "(Last+Updated: 12/17/2021",
      "assignments": [
        {
          "assignment": "Loops and lists",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "10/12/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Loops",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "10/04/2021",
          "score": "CWS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Collections",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/30/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Classes and structures",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "08/27/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Programmatically creating UI components",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "08/27/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Creating simple UI components",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "08/27/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Introductory Swift",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "08/19/2021",
          "score": "CWS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "App dev cycle",
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
      "Last Updated": "(Last+Updated: 12/26/2021",
      "assignments": [
        {
          "assignment": "MP2 Package/Segment",
          "category": "Major Grades",
          "dateAssigned": "09/27/2021",
          "dateDue": "10/15/2021",
          "score": "83.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "PA Script #4",
          "category": "Minor Grades",
          "dateAssigned": "09/24/2021",
          "dateDue": "10/15/2021",
          "score": "95.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Show Elements (Show Open, Graphics, etc)",
          "category": "Minor Grades",
          "dateAssigned": "08/16/2021",
          "dateDue": "10/15/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Social Media Post #2",
          "category": "Minor Grades",
          "dateAssigned": "09/27/2021",
          "dateDue": "10/15/2021",
          "score": "91.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "PA Script #3",
          "category": "Minor Grades",
          "dateAssigned": "09/20/2021",
          "dateDue": "10/15/2021",
          "score": "89.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Event Coverage",
          "category": "Major Grades",
          "dateAssigned": "08/12/2021",
          "dateDue": "10/07/2021",
          "score": "60.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "MP1 Package/Segment #1",
          "category": "Major Grades",
          "dateAssigned": "08/16/2021",
          "dateDue": "09/24/2021",
          "score": "97.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Social Media Post #1",
          "category": "Minor Grades",
          "dateAssigned": "08/24/2021",
          "dateDue": "09/24/2021",
          "score": "98.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "PA Script #2",
          "category": "Minor Grades",
          "dateAssigned": "09/01/2021",
          "dateDue": "09/17/2021",
          "score": "93.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "PA Script #1",
          "category": "Minor Grades",
          "dateAssigned": "08/12/2021",
          "dateDue": "08/31/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Practicum Training Plan",
          "category": "Minor Grades",
          "dateAssigned": "08/12/2021",
          "dateDue": "08/26/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "MP1 Calendar Check",
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
      "Last Updated": "(Last+Updated: 12/17/2021",
      "assignments": [
        {
          "assignment": "Timed Write #2",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "10/05/2021",
          "score": "85.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Macbeth Soliloquy",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "10/04/2021",
          "score": "85.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "College Essay",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/17/2021",
          "score": "85.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Macbeth Quiz",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/14/2021",
          "score": "92.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Macbeth Timed Writing",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/01/2021",
          "score": "80.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "College Essay OUTLINE, 10C",
          "category": "Minor Grades",
          "dateAssigned": "08/27/2021",
          "dateDue": "08/27/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Macbeth Pre-Reading Questions, 4F",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "08/20/2021",
          "score": "80.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Intro Letter, 9E",
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
      "Last Updated": "(Last+Updated: 12/8/2021",
      "assignments": [
        {
          "assignment": "Unit 2 Test (Limit Def'n of Deriv, Basic Derivative Rules)",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "10/07/2021",
          "score": "85.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "2.4,2.6 Delta Math Practice",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "10/05/2021",
          "score": "94.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "2.3,2.5 Delta Math Practice",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/24/2021",
          "score": "96.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "2.1-2.2 Delta Math Practice",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/20/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 Test (Limits)",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/09/2021",
          "score": "83.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "1.7-1.8 Delta Math Average",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/01/2021",
          "score": "90.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "1.4-1.6 Delta Math Practice",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "08/30/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "1.1-1.3 Delta Math Average",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "08/20/2021",
          "score": "89.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "1.2 Skills Check (Limits Graphically)",
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
      "Last Updated": "(Last+Updated: 12/17/2021",
      "assignments": [
        {
          "assignment": "Test - 3.2 Least Squares Regression",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "10/07/2021",
          "score": "71.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Test - 3.1 Scatterplots and Correlation",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "10/07/2021",
          "score": "71.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Review - 3 Describing Relationships",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "10/07/2021",
          "score": "58.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Skills Check - 3.2 LSRL, Residuals, and Residual Plots",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "10/04/2021",
          "score": "89.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Skills Check - 3.1 Scatterplots and Correlation",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/30/2021",
          "score": "79.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Test - 2.2 Normal Distributions",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/24/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Test - 2.1 Describing Location",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/24/2021",
          "score": "92.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Review - 2 Modeling Distributions of Data",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/24/2021",
          "score": "91.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Skills Check - 2.2 Density Curves and Normal Distributions",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/20/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Practice - 2.2 Normal Distributions",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/20/2021",
          "score": "L",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Practice - 2.2 Density Curves and the Empirical Rule",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/20/2021",
          "score": "60.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Skills Check - 2.1 Describing Location",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/16/2021",
          "score": "92.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Practice - 2.1",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/16/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Test - 1 Exploring Data",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/08/2021",
          "score": "89.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Quiz - 1 Exploring Data",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/02/2021",
          "score": "89.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Skills Check - 1.1 Analyzing Categorical Data",
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
      "Last Updated": "(Last+Updated: 12/17/2021",
      "assignments": [
        {
          "assignment": "Unit 2 Assessment - Biodiversity_all topics",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "10/13/2021",
          "score": "86.67",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 2 QUIZ - Topics 2.1-2.3",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "10/06/2021",
          "score": "86.67",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 2 - Island Biogeography Lab",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "10/04/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 - Ecosystem project",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/24/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 Assessment - all Topics",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/22/2021",
          "score": "91.67",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 - Topics 1.8-1.11 QUIZ",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/16/2021",
          "score": "93.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Owl Pellet Lab- Flow of Energy",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/16/2021",
          "score": "97.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 - Topics 1.4-1.7 QUIZ (BGC cycles)",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/02/2021",
          "score": "95.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Bozeman- BGC Cycles Performance Task",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/02/2021",
          "score": "96.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 - Topics 1.1 - 1.3 QUIZ",
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
      "Last Updated": "(Last+Updated: 12/10/2021",
      "assignments": [
        {
          "assignment": "Units 1-3 FRQ Test: Choice #2",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/27/2021",
          "score": "88.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Units 1-3 FRQ Test: Choice #1",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/27/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Units 1-3 FRQ Test: Required Question",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/27/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Units 1-3 MCQ Test: Unit 3 Topic",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/27/2021",
          "score": "94.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Units 1-3 MCQ Test: Unit 2 Topic",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/27/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Units 1-3 MCQ Test: Unit 1 Topic",
          "category": "Major Grades",
          "dateAssigned": "",
          "dateDue": "09/27/2021",
          "score": "79.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 3 FRQ Quiz",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/23/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 3 MCQ Quiz",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/23/2021",
          "score": "96.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 3 AP Classroom Progress Check MCQ",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/21/2021",
          "score": "INS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 3.5: Return to LRAS",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/17/2021",
          "score": "INS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 3.3: Fiscal Policy",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/15/2021",
          "score": "INS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 3.2: Potential Output and Gaps",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/13/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 3.1: AD/SRAS/LRAS",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/09/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 2 FRQ Quiz",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/09/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 2 MCQ Quiz",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "09/09/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 2 AP Classroom Progress Check MCQ",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/07/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 2.4: Business Cycle",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/01/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 2.3: Inflation",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "09/01/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 2.2: Unemployment",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "08/30/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 2.1: Circular Flow and GDP",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "08/26/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 FRQ Quiz",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "08/26/2021",
          "score": "100.0",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 MCQ Quiz",
          "category": "Minor Grades",
          "dateAssigned": "",
          "dateDue": "08/26/2021",
          "score": "88.00",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Unit 1 AP Classroom Progress Check MCQ",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "08/24/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 1.4: Double Shifts & Disequilibrium",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "08/20/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 1.3: Micro Markets",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "08/18/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 1.2: Production Possibilities Curve",
          "category": "Non-graded",
          "dateAssigned": "",
          "dateDue": "08/16/2021",
          "score": "CNS",
          "totalPoints": "100.00"
        },
        {
          "assignment": "Flipped Video 1.1: Scarcity",
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
}
```