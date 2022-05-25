---
sidebar_position: 4
---

# [GET] Student Current Classes Information

Get information on each class a student is taking including assignments and grades

```http
GET /students/currentclasses?username={username}&password={password}
```

### Query Parameters
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. HAC username|
| `password` | `string` | **Required**. HAC password|

### Example Requests

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs
  defaultValue="Node.js"
>
<TabItem value="Node.js" label="Node.js (Axios)">

```js
axios.get("https://gradual-deploy.vercel.app/students/currentclasses?username=john&password=doe").then((res) => {
    console.log(res.data);
}).catch((error) => {
    console.log(error);
})
```

</TabItem>
<TabItem value="Javascript (Fetch)">

```js
fetch("https://gradual-deploy.vercel.app/students/currentclasses?username=john&password=doe", { 
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

reqUrl = "https://gradual-deploy.vercel.app/students/currentclasses?username=john&password=doe"

payload = ""

response = requests.request("GET", reqUrl, data=payload)

print(response.text)
```

</TabItem>

<TabItem value="C#">

```cs
var client = new HttpClient();
var request = new HttpRequestMessage();
request.RequestUri = new Uri("https://gradual-deploy.vercel.app/students/currentclasses?username=john&password=doe");
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
  'https://gradual-deploy.vercel.app/students/currentclasses?username=john&password=doe' \
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