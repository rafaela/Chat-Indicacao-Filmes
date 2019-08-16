const express = require('express') 
const chatService = require('../api/chat/chatService')
const filmesService = require('../api/filmes/filmesService')
const chatBot = require('../api/chatbot/chatbot')

module.exports = function (server) {

    const api = express.Router()
    server.use('/api', api)

    api.post('/chat', (req, res) => {

        if (!req.body.message) {
            res.status(403).send({ errors: ['No message provided.'] })
            return;
        }

        chatBot.analisarConstruirMensagem({
            session_id: req.body.session_id,
            message: {
                text: req.body.message
            }
        })
            .then((user) => {

                user.save((err) => {
                    if (err) {
                        console.log(err);
                        res.send(err);
                    } else {
                        res.status(201).json(user);
                    }
                })
            })
    })

    chatService.register(api, '/chat')
    filmesService.register(api, '/filmes') 
}