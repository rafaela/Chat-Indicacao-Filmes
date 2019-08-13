require('dotenv').config()
const mongoose = require('mongoose')
mongoose.Promise = global.Promise

const uri = 'mongodb://localhost/indicacao-filmes' || process.env.MONGODB_URI ;
console.log(uri)

module.exports = mongoose.connect(uri, {useMongoClient: true})