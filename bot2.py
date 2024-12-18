import asyncio
import logging
from aiogram import F, Bot, Dispatcher,types
from aiogram.filters import Command
from aiogram.types import Message


logging.basicConfig(level=logging.INFO)
bot = Bot(token='7665892266:AAGhSzCqlOnSfOBfqZFj44t9F7xhyKvPSik')
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_name(message: Message):
    await message.answer("Привет, я тестовый бот")

@dp.message(Command("info"))
async def cmd_name(message: Message):
    await message.reply("У меня есть следующие команды \n /start \n /info")

@dp.message(Command("name")) 
async def cmd_hello(message: Message): 
    args = message.text.split(maxsplit=1) 
    if len(args) > 1: 
        await message.answer(f"Привет, <b>{args[1]}</b>", parse_mode="HTML") 
    else: 
        await message.answer("Пожалуйста, укажи своё имя после команды /name!") 

@dp.message(Command("test"))
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2") 



@dp.message(Command("button")) 
async def cmd_start(message: Message): 
    kb = [ 
        [types.KeyboardButton(text="Первая кнопка")], 
        [types.KeyboardButton(text="Вторая кнопка")]

    ] 
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb) 
    await message.answer("Какую кнопку вы выбрали?", reply_markup=keyboard  ) 
 
@dp.message(lambda message: message.text == "Первая кнопка") 
async def first_btn(message: Message): 
    await message.reply("Вы нажали первую кнопку") 
 
@dp.message(lambda message: message.text == "Вторая кнопка") 
async def second_btn(message: Message): 
    await message.reply("Вы нажали вторую кнопку") 



@dp.message(Command("special_buttons")) 
async def cmd_special_buttons(message: types.Message): 
    kb = [
        [types.KeyboardButton(text="Запросить контакт", request_contact=True)],
        [types.KeyboardButton(text="Запросить викторину", request_poll=types.KeyboardButtonPollType(type='quiz'))],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)  
    await message.reply("Выберите действие", reply_markup=keyboard)


@dp.message(lambda message: message.text == "Запросить викторину")
async def send_quiz(message: types.Message):
    question = "Какой самый большой океан на Земле?"
    options = ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"]
    correct_option_id = 2 
    
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type='quiz',
        correct_option_id=correct_option_id,
        is_anonymous=False  
    )

@dp.message(F.content_type == "animation")
async def echo_gif(message: Message):
    await message.reply_animation(message.animation.file_id) 


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

