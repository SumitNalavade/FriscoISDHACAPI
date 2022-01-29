//Take in a function, execute and call next() if there is an async error
module.exports = (func) => {
    return (req, res, next) => {
        func(req, res, next).catch(next);
    }
}