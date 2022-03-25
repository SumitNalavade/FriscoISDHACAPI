const { default: axios } = require("axios");

module.exports = async (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    const { username, password, quarter } = req.query;

    const { data } = await axios.get(`https://gradualgrades.herokuapp.com/students/currentclasses?username=${username}&password=${password}&quarter=${quarter}`);

    return res.send(data)

    return res.status(500).send(error.response.data)
}