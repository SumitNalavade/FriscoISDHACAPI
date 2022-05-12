# [GET] Student GPAs

Get a students most recently published weighted and unweighted GPA from HAC

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

<Tabs>
  <TabItem value="Node.js" label="Node.js (Axios)"> 
  </TabItem>

  <TabItem value="Javascript" label="Javascript (Fetch)">
  </TabItem>

  <TabItem value="Python" label="Python (Requests)">
  </TabItem>

  <TabItem value="cURL" label="cURL" default>
  </TabItem>
</Tabs>