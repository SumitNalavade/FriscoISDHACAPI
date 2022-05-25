---
sidebar_position: 3
---

# [GET] Student Schedule

Get a student's schedule

```http
GET /students/schedule?username={username}&password={password}
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
axios.get("https://gradual-deploy.vercel.app/students/schedule?username=john&password=doe").then((res) => {
    console.log(res.data);
}).catch((error) => {
    console.log(error);
})
```

</TabItem>
<TabItem value="Javascript (Fetch)">

```js
fetch("https://gradual-deploy.vercel.app/students/schedule?username=john&password=doe", { 
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

reqUrl = "https://gradual-deploy.vercel.app/students/schedule?username=john&password=doe"

payload = ""

response = requests.request("GET", reqUrl, data=payload)

print(response.text)
```

</TabItem>

<TabItem value="C#">

```cs
var client = new HttpClient();
var request = new HttpRequestMessage();
request.RequestUri = new Uri("https://gradual-deploy.vercel.app/students/schedule?username=john&password=doe");
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
  'https://gradual-deploy.vercel.app/students/schedule?username=john&password=doe' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)'
```

</TabItem>
</Tabs>

### Example Response
```json
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