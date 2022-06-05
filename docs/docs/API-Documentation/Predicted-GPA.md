# [POST] Student Predicted Real-time GPA

Get a students predicted GPA with their current grades

```http
POST /predictedGPA
```

### Query Parameters
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `weightedGPA` | `number` | **Required**. Student's weighted GPA in HAC|
| `unweightedGPA` | `number` | **Required**. Student's unweighted GPA in HAC|
| `studentGrade` | `number` | **Required**. Student's current grade level|
| `studentGrade` | `array` | **Required**. Array of student class objects (You can use /students/currentClasses to get this)|

### Example Requests

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs
  defaultValue="Node.js"
>
<TabItem value="Node.js" label="Node.js (Axios)">

```js
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

</TabItem>
<TabItem value="Javascript (Fetch)">

```js
let bodyContent = JSON.stringify({
"weightedGPA": 5.05,
"unweightedGPA": 3.88,
"studentGrade": 12,
"currentClasses": [
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
});

fetch("https://gradual-deploy.vercel.app/predictedGPA", { 
  method: "POST",
  body: bodyContent
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
import json

url = "https://gradual-deploy.vercel.app/predictedGPA"

payload = json.dumps({
  "weightedGPA": 5.05,
  "unweightedGPA": 3.88,
  "studentGrade": 12,
  "currentClasses": [
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
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

</TabItem>

<TabItem value="Swift">

```swift
import Foundation
#if canImport(FoundationNetworking)
  import FoundationNetworking
#endif

var parameters = ""
        let semaphore = DispatchSemaphore (value: 0)

        let data: [String: Any] = [
            "weightedGPA": 5.05,
            "unweightedGPA": 3.88,
            "studentGrade": 12,
            "currentClasses": [
                [
                  "name": "CATE27600A - 3    Mobile App Programming S1@CTEC",
                  "grade": 100,
                  "weight": 6,
                  "credits": 1
                ],
                [
                  "name": "CATE36400A - 1    Prac News Prod 2 S1",
                  "grade": 91.48,
                  "weight": 5,
                  "credits": 1
                ],
                [
                  "name": "ELA14300A - 4    AP English Literature S1",
                  "grade": 88.13,
                  "weight": 6,
                  "credits": 1
                ],
                [
                  "name": "MTH45300A - 1    AP Calculus AB S1",
                  "grade": 79.4,
                  "weight": 6,
                  "credits": 1
                ],
                [
                  "name": "MTH45310A - 4    AP Statistics S1",
                  "grade": 79.48,
                  "weight": 6,
                  "credits": 1
                ],
                [
                  "name": "SCI43300A - 1    AP Environmental Science S1",
                  "grade": 94,
                  "weight": 6,
                  "credits": 1
                ],
                [
                  "name": "SST34310 - 3    AP Economics",
                  "grade": 93.24,
                  "weight": 6,
                  "credits": 1
                ]
            ]
        ]
        
        
        do {
            let data1 =  try JSONSerialization.data(withJSONObject: data, options: JSONSerialization.WritingOptions.prettyPrinted) // first of all convert json to the data
            parameters = String(data: data1, encoding: String.Encoding.utf8)! // the data will be converted to the string
               } catch let myJSONError {
                   print(myJSONError)
               }
        
        let postData = parameters.data(using: .utf8)

        var request = URLRequest(url: URL(string: "https://gradual-deploy.vercel.app/predictedGPA")!,timeoutInterval: Double.infinity)
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")

        request.httpMethod = "POST"
        request.httpBody = postData

        let task = URLSession.shared.dataTask(with: request) { data, response, error in
          guard let data = data else {
            print(String(describing: error))
            semaphore.signal()
            return
          }
          print(String(data: data, encoding: .utf8)!)
          semaphore.signal()
        }

        task.resume()
        semaphore.wait()
```

</TabItem>

<TabItem value="Dart">

```dart
var headers = {
  'Content-Type': 'application/json'
};
var request = http.Request('POST', Uri.parse('https://gradual-deploy.vercel.app/predictedGPA'));
request.body = json.encode({
  "weightedGPA": 5.05,
  "unweightedGPA": 3.88,
  "studentGrade": 12,
  "currentClasses": [
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
});
request.headers.addAll(headers);

http.StreamedResponse response = await request.send();

if (response.statusCode == 200) {
  print(await response.stream.bytesToString());
}
else {
  print(response.reasonPhrase);
}
```

</TabItem>

<TabItem value="C#">

```cs
var client = new HttpClient();
var request = new HttpRequestMessage();
request.RequestUri = new Uri("https://gradual-deploy.vercel.app/predictedGPA");
request.Method = HttpMethod.Post;

request.Headers.Add("Accept", "*/*");
request.Headers.Add("User-Agent", "Thunder Client (https://www.thunderclient.com)");

var bodyString = "{\"weightedGPA\": 5.05,\"unweightedGPA\": 3.88,\"studentGrade\": 12,\"currentClasses\": [        {          \"name\": \"CATE27600A - 3    Mobile App Programming S1@CTEC\",          \"grade\": 100,          \"weight\": 6,          \"credits\": 1        },        {          \"name\": \"CATE36400A - 1    Prac News Prod 2 S1\",          \"grade\": 91.48,          \"weight\": 5,          \"credits\": 1        },        {          \"name\": \"ELA14300A - 4    AP English Literature S1\",          \"grade\": 88.13,          \"weight\": 6,          \"credits\": 1        },        {          \"name\": \"MTH45300A - 1    AP Calculus AB S1\",          \"grade\": 79.4,          \"weight\": 6,          \"credits\": 1        },        {          \"name\": \"MTH45310A - 4    AP Statistics S1\",          \"grade\": 79.48,          \"weight\": 6,          \"credits\": 1        },        {          \"name\": \"SCI43300A - 1    AP Environmental Science S1\",          \"grade\": 94,          \"weight\": 6,          \"credits\": 1        },        {          \"name\": \"SST34310 - 3    AP Economics\",          \"grade\": 93.24,          \"weight\": 6,          \"credits\": 1        }      ]}";
var content = new StringContent(bodyString, Encoding.UTF8, "application/json");
request.Content = content;

var response = await client.SendAsync(request);
var result = await response.Content.ReadAsStringAsync();
Console.WriteLine(result);
```

</TabItem>
</Tabs>

### Example Response
```json
{
  "finalWeightedGPA": "5.018267857142857",
  "finalUnweightedGPA": "3.8539464285714287"
}
```