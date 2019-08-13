const restful = require('node-restful')
const mongoose = restful.mongoose

const messageSchema = new mongoose.Schema({
    message: {
        type: String,
        required: true
    },
    base: {
        type: String,
        default: 'sent'
    },
    sendAt: {
        type: Date,
        default: Date.now
    }
})

const chatSchema = new mongoose.Schema({
    session_id: { 
        type: String 
    },
    context: {},
    userName: { 
        type: String 
    },
    input: {},
    messages: [messageSchema]
}, { usePushEach: true })

module.exports = restful.model('Chat', chatSchema)