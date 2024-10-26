const TelegramBot = require('node-telegram-bot-api');
const express = require('express');
const cors = require('cors');

const token = '7337113069:AAELTI93Yezh_3LYzPSvw-U3eXP90c63PTc';
const webAppUrl = 'https://effervescent-cajeta-34bc49.netlify.app/';

const bot = new TelegramBot(token, {polling: true});
const app = express();

app.use(express.json());
app.use(cors());

let formArray = [];

const generateContract = () => {
    return Math.floor(100000000 + Math.random() * 900000000).toString(); 
};

app.post('/registration', (req, res) => {
    const {fullName, phone, email, address} = req.body;
    const contract = generateContract();
    formArray.push({fullName, phone, email, address, contract}) 
    console.log('Массив данных: ',formArray)
    res.status(201).json({message: formArray})
})
app.get('/registration', (req, res) => {
    res.status(200).json(formArray);
});
bot.on('message', async (msg) => {
    const chatId = msg.chat.id;
    const text = msg.text;

    if(text === '/start') {
        await bot.sendMessage(chatId, 'Проверка формы', {
            reply_markup: {
                inline_keyboard: [
                    [{text: 'Открыть', web_app: {url: webAppUrl}}]
                ]
            }
        })
    }})

const PORT = 8000;

app.listen(PORT, () => console.log('server started on PORT ' + PORT))