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

app.get("/students/info/", async (req, res) => {
    const { username, password } = req.query;

    const { data } = await axios.get(`https://gradualgrades.herokuapp.com/students/info?username=${username}&password=${password}`);

    res.send(data)
});

app.get("/students/currentclasses/", async (req, res) => {
    const { username, password } = req.query;

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