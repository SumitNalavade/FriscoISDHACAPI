const { default: axios } = require("axios");
const express = require("express")
const cors = require("cors");
const app = express();
app.use(cors({
    origin: '*'
}));
app.use(express.json())
const PORT = process.env.PORT || 3000

app.listen(PORT, (req, res) => {
    console.log(`Express app listening on port ${PORT}`)
});

app.get("/", async (req, res) => {
    const { data } = await axios.get("https://gradualgrades.herokuapp.com/")

    return res.send(data)
});

app.get("/students/gpa/:username/:password", async (req, res) => {
    const { username, password } = req.params;

    const { data } = await axios.get(`https://gradualgrades.herokuapp.com/students/gpa?username=${username}&password=${password}`);

    res.send(data)
});

app.get("/students/info/:username/:password", async (req, res, next) => {
    try {
        const { username, password } = req.params;

        const { data } = await axios.get(`https://gradualgrades.herokuapp.com/students/info?username=${username}&password=${password}`);
    
        res.send(data)
    } catch(error) {
        next(error)
    }
});

app.get("/students/currentclasses/:username/:password", async (req, res) => {
    const { username, password } = req.params;

    const { data } = await axios.get(`https://gradualgrades.herokuapp.com/students/currentclasses?username=${username}&password=${password}`);

    res.send(data)
});

app.post("/predictedGPA/", async(req, res) => {
    const { weightedGPA, unweightedGPA, studentGrade, currentClasses } = req.body;

    const { data } = await axios.post(`https://gradualgrades.herokuapp.com/predictedGPA`, {
        weightedGPA,
        unweightedGPA,
        studentGrade,
        currentClasses
    });

    return res.send(data);
});

app.get("/satdates", async (req, res) => {
    const { data } = await axios.get("https://gradualgrades.herokuapp.com/satdates");

    return res.send(data);
});

app.use((err, req, res, next) => {
    const { status=500, statusText="Internal Server Error" } = err.response;

    return res.status(status).send(statusText);
});