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

<TabItem value="Swift">

```swift
import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif


//Define a function to get the data from the API
func getData(_ completion: @escaping ([String: String]) -> ()) {
  let urlPath = "https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe"
        
  guard let url = URL(string: urlPath) else { return }
        
  let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
    guard let data = data else { return }
      do {
        if let jsonResult = try JSONSerialization.jsonObject(with: data, options: JSONSerialization.ReadingOptions.mutableContainers) as? NSDictionary {
            let results = jsonResult as! [String: String]
                    completion(results)
          }
            } catch {
                
            }
        }
  task.resume()
}

//Call the function and print the data
getData{ (studentData) in
    print(studentData)
}
```

</TabItem>

<TabItem value="Dart">

```Dart
var request = http.Request('GET', Uri.parse('https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe'));
request.body = '''''';

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
request.RequestUri = new Uri("https://gradual-deploy.vercel.app/students/gpa?username=john&password=doe");
request.Method = HttpMethod.Get;

request.Headers.Add("Accept", "*/*");
request.Headers.Add("User-Agent", "Thunder Client (https://www.thunderclient.com)");

var response = await client.SendAsync(request);
var result = await response.Content.ReadAsStringAsync();
Console.WriteLine(result);
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