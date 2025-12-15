 
# Frisco ISD HAC API  
REST API to access student data from Home Access Center (Frisco ISD)   

# API Documentation
https://friscoisdhacapi.vercel.app/

# Base API Endpoint
https://friscoisdhacapi.vercel.app/api





## License  
[Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/)

## Run Locally  
Clone the project  

~~~bash  
  git clone https://github.com/SumitNalavade/FriscoISDHACAPI.git
~~~

Go to the project directory  

~~~bash  
  cd FriscoISDHACAPI
~~~

Install dependencies  

~~~bash  
npm install
~~~

Start the development server  

~~~bash  
npm run dev
~~~  

Access API Routes
~~~bash  
http://localhost:3000/api/...
~~~  
## Production Usage (Self-Host Guide)
Because the public deployment enforces shared rate limits, you should deploy your own copy of this API for production use. This project is implemented as serverless functions and works best on a platform like Vercel that supports Next.js serverless + Edge middleware.

## 1. Fork or Clone the Repository
Fork the repository on GitHub so you can deploy it directly from your own account.

## 2. Deploy on Vercel
- Go to Vercel → Add New → Project
- Import your forked GitHub repository
- Select Next.js as the framework preset
- Deploy the Project

## 3. Access deployed API Routes
~~~bash  
  https://[deployment-url]/api/...
~~~