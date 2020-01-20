from pyrogram import (
    Client, Filters, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
)
from uuid import uuid4
from secure import *
from random import randint


app = Client(BOT_TOKEN, API_ID, API_HASH, proxy=PROXY)


@app.on_message(Filters.command(['start', 'help']))
def start(client, message):
    message.reply(
        f'Добрый день. Этот бот поможет вам провести видеозвонок с другими пользователями Telegram. Для этого введите `@{app.get_me().username}` в личные сообщения или в группу с теми, кому вы хотите позвонить, и нажмите "Начать звонок".')

@app.on_inline_query()
def inline(client, inline_query):
    room_id = str(randint(10**5, 10**16))
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                id=uuid4(),
                title='Начать видеозвонок',
                description='Все участники чата смогут присоединиться',
                input_message_content=InputTextMessageContent(
                    f'{inline_query.from_user.first_name} начал видеозвонок'
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton('📞 Присоединиться', url='https://appr.tc/r/'+room_id)]
                    ]
                )
            )
        ],
        cache_time=0, is_personal=True
    )


app.run()