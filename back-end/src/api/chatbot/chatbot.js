require('dotenv').config()
const AssistantV1 =  require('ibm-watson/assistant/v1');
const chatService = require('../chat/chatService')
const filmesService = require('../filmes/filmesService')

const assistant = new AssistantV1({
    username: process.env.WATSON_USERNAME,
    password: process.env.WATSON_PASSWORD,
    version: process.env.WATSON_VERSION
});

iniciarOuContinuarConversa = (input) => new Promise((resolve, reject) => {
    chatService.find({ session_id: input.session_id }, (err, data) => {
        if (err || data.length == 0 || data == undefined) {

            let chat = new chatService({
                input: input.message || undefined,
                session_id: undefined,
            });
            chat.session_id = chat._id;

            resolve(chat);
        }
        else {
            chat = data[0];
            chat.input = input.message || undefined,
            resolve(chat);
        }
    })
});
