const { default: axios } = require("axios");
const cors = require("cors");
app.use(cors({
    origin: '*'
}));

module.exports = async (req, res) => {
    const { data } = await axios.get("https://gradualgrades.herokuapp.com/satdates");

    return res.send(data);
}