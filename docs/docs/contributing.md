# Contributing

Contributions are always welcome!

Please make sure all changes are throughly tested with all routes before submitting a pull request

### Run locally

Clone the repo
```bash
git clone https://github.com/SumitNalavade/FriscoISDHACAPI.git
```

Change directory to repo
```bash
cd FriscoISDHACAPI
```

Install dependencies
```bash
pip install -r requirements.txt
```

Start Flask server
```bash
export FLASK_APP=flaskapp
export FLASK_DEBUG=1
flask run
```

You can now run the api locally using 'localhost:5000' as the base URL

Example:
http://localhost:5000/students/currentclasses?username=john&password=doe