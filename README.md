# Frisco ISD HAC API
REST API to access student info from the Frisco ISD Home Access Center

# API Documentation
https://friscoisdhacapidocs.vercel.app/


## Python vs Golang API Loading Time ⏳

After rewriting our API in Go instead of Python, we were able to experience a significant improvement in our response times thanks to the ability to spawn Goroutines to scrape individual elements from HAC concurrently in Go. 

The data below shows our results after 10 trials in each language (less is better).

| API Load Time (Milliseconds) | Python | Go (No Concurrency) | Go (Concurrent) |
| --- | --- | --- | --- |
|  | 1170 | 849 | 632 |
|  | 1370 | 1120 | 1050 |
|  | 1140 | 858 | 956 |
|  | 861 | 914 | 649 |
|  | 1220 | 1170 | 847 |
|  | 1130 | 1000 | 627 |
|  | 1030 | 2360 | 651 |
|  | 1130 | 964 | 767 |
|  | 1120 | 1020 | 1060 |
|  | 1180 | 724 | 729 |
| Average | 1135.1 | 1097.9 | 796.8 |

Average API response time for the ```/students/schedule``` route after 10 trials each.

Data shows ✨ <b>~ 70.1965% decrease </b> in loading times after rewriting API in Go (concurrent).

### Two sample ‘T’ test for significance

$H_0 =$  No significant difference between response times for Python & Go (concurrent) API

$H_a$ = Significant difference between response times for Python & Go (concurrent) API

$a = 0.05$

$p = 0.0394$

Because the $p$ value, 0.0394 is less than our $a=0.05$, we <b>reject the null hypothesis</b>, there is a significant difference in API response time when rewriting the API in Go.

## Contributing  

Contributions are always welcome!  

See `contributing.md` for ways to get started.  

Please adhere to this project's `code of conduct`.  

## License  

[MIT](https://choosealicense.com/licenses/mit/)
