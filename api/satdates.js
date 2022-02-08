const { default: axios } = require("axios");

module.exports = async (req, res) => {
    const { data } = await axios.get("https://gradualgrades.herokuapp.com/satdates");

    return res.send(data);
}