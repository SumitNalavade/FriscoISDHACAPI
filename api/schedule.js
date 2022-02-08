const { default: axios } = require("axios");
const cors = require("cors");
app.use(cors({
    origin: '*'
}));

module.exports = async (req, res) => {
    const { username, password } = req.query;

    const { data } = await axios.get(`https://gradualgrades.herokuapp.com/students/schedule?username=${username}&password=${password}`);

    return res.send(data)

    return res.status(500).send(error.response.data)
}