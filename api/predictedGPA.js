const { default: axios } = require("axios");
const { micro } = require("micro-cors");

async function predictedGPA(req, res) {
    if (req.method === "OPTIONS") {
      return res.status(200).end();
    }
    
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

const cors = micro();

export default cors(MyApi);
