const { default: axios } = require("axios");

module.exports = async (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    const { data } = await axios.get(`https://gradualgrades.herokuapp.com/`);

    return res.send(data)

    return res.status(500).send(error.response.data)
}