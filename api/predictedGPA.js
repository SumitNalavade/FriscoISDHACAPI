const { default: axios } = require("axios");

module.exports = async (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    const { weightedGPA, unweightedGPA, studentGrade, currentClasses } = req.body;

    const { data } = await axios.post(`https://gradualgrades.herokuapp.com/predictedGPA`, {
        weightedGPA,
        unweightedGPA,
        studentGrade,
        currentClasses
    });

    return res.send(data);
}