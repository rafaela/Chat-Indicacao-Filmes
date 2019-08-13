const filmesService = require('./filmesService')
const fs = require('fs');
const filmes = require('../dados/avaliacaoFilmesGenero')
 


// Função exportada que, caso não exista produtos no banco, cria exemplos (MOCK)
module.exports.checkDataBase = () => {
    filmesService.find({}, (err, data) => {
        if (err || data.length <= 0 || data == undefined) {
            // Iteração com cada produto da lista produtos
            filmes.forEach(filme => {
                new filmesService(filme).save()
            });
            console.log("Banco criado");
        }
    })
};