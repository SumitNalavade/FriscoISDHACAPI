---
sidebar_position: 1
---

# Frisco ISD HAC API

REST API to scrape student information from Frisco ISD's Home Access Center (HAC) using python requests and Beautiful Soup

Powers the Gradual Grades mobile app developed with @mjdierkes. https://github.com/mjdierkes

# Base API URL
https://gradual-deploy.vercel.app

# Routes
 - GET student GPAs
 - GET student information
 - GET student schedule
 - GET student class data with assignment details for current quarter
 - GET student class data with assignment details for ANY QUARTER
 - POST get student predicted GPAs

# Technologies Used
 - Python
 - Flask
 - BeautifulSoup
 - Heroku
 - Vercel

# Behind the scenes
The API uses sends HTTP POST requests to Frisco ISD HAC servers with a username and password.

If the login is authenticated, HAC responds with an HTML page with student information.

The resulting HTML page is then parsed using the BeautifulSoup library and the requested information is extracted from the markup.

# Security
No user information is stored in any databases. All of the proccessing that happens in a request is dumped once the request has resolved.

# Feedback
If you have any feedback, please reach out to me at vs.nalavade2003@gmail.com

# License
[Creative Commons ShareAlike 4.0]https://creativecommons.org/licenses/by-sa/4.0/