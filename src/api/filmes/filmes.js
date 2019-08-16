const restful = require('node-restful')
const mongoose = restful.mongoose


const filmesSchema = new mongoose.Schema({
    titulo: { type: String, required: true },
    imagem:{ type: String,  required: true },
    categoria:{ type: String,  required: true },
    genero: [],
    generos_id: [],
    resumo: { type: String },
    diretor: {type: String },
    elenco: [],
    classificacao:{ type: String },
    avaliacao:{ type: String },
    duracao:{ type: String },
    ano:{ type: String },
    colocaco:{ type: String }

})

module.exports = restful.model('Filmes', filmesSchema)
