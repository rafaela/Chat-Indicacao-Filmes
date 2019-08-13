const filmes = require('./filmes')

filmes.methods(['get', 'post', 'put', 'delete'])
filmes.updateOptions({new: true, runValidators: true})

module.exports = filmes