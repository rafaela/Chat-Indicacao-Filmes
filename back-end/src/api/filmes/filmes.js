const restful = require('node-restful')
const mongoose = restful.mongoose


const filmesSchema = new mongoose.Schema({
    titulo: {
        type: String, 
        required: true
    },
    imagem:{
        type: String, 
        required: true
    },
    genero: [],
    resumo: {
        type: String, 
        required: true
    },
    diretor: {
        type: String, 
        required: true
    },
    elenco: [],
    classificacao:{
        type: String, 
        required: true
    },
    avaliacao:{
        type: String, 
        required: true
    },
    duracao:{
        type: String, 
        required: true
    },
    ano:{
        type: String, 
        required: true
    }

})

module.exports = restful.model('Filmes', filmesSchema)