---
sidebar_position: 2
---


# [GET] Student GPAs

Get a student's most recently published weighted and unweighted GPA from HAC

```http
GET /students/gpa?username={username}&password={password}
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
axios.get("https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe").then((res) => {
    console.log(res.data); //Make sure to denote what data you want from the response
}).catch((error) => {
    console.log(error);
})
```

</TabItem>
<TabItem value="Javascript (Fetch)">

```js
fetch("https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe", { 
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

reqUrl = "https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe"

payload = ""

response = requests.request("GET", reqUrl, data=payload)

print(response.text)
```

</TabItem>

<TabItem value="C#">

```cs
var client = new HttpClient();
var request = new HttpRequestMessage();
request.RequestUri = new Uri("https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe");
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
  'https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)'
```

</TabItem>
</Tabs>

### Example Response
```json
{
    "unweightedGPA" : "3.8800",
    "weightedGPA" : "5.0500"
}
```