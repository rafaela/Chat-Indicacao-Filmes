const filmesMock = require('../api/filmes/filmesMock')

const options = {
    host: "localhost",
    port: process.env.PORT || 3003
};

const bodyParser = require('body-parser')
const express = require('express')
const allowCors = require('./cors')
const queryParser = require('express-query-int')
const server = express()


server.use(bodyParser.urlencoded({ extended: true })) 
server.use(bodyParser.json()) 
server.use(allowCors) 
server.use(queryParser())

server.listen(options, function(){
    filmesMock.checkDataBase();
    console.log(`Backend está rodando em http://${options.host}:${options.port}/`);
}) 

module.exports = server