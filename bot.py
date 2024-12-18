import asyncio
import logging
from aiogram import Bot, Dispatcher,types,F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton,ReplyKeyboardMarkup,ContentType 
import random
import requests

import pyttsx3
import subprocess

logging.basicConfig(level=logging.INFO)
bot = Bot(token='7268270239:AAEEiFKYCavT-ApDbkAR84BnuYXNeVv0nFU')
dp = Dispatcher()



@dp.message(Command("game"))
async def launch_game(message: Message):
    def run_game():
        try:
            subprocess.Popen(r"C:\Users\danii\AppData\Roaming\.minecraft\TLauncher.exe")
            return "Игра запущена!"
        except FileNotFoundError:
            return "Путь к игре не найден. Проверьте путь в коде."

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_game)

    await message.reply(response)





btn_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Хоррор")],
        [KeyboardButton(text="Экшн")],
        [KeyboardButton(text="Юмор")],
        [KeyboardButton(text="Фантастика")]
    ],
    resize_keyboard=True
)

horror = ["https://www.kinopoisk.ru/series/589167/","https://www.kinopoisk.ru/film/4530564/"]
action = ["https://www.kinopoisk.ru/film/444/","https://www.kinopoisk.ru/film/597687/","https://www.kinopoisk.ru/film/463354/"]
fantastic = ["https://www.kinopoisk.ru/film/7410/","https://www.kinopoisk.ru/film/437678/","https://www.kinopoisk.ru/film/496888/"]
humor = ["https://www.kinopoisk.ru/series/258382/","https://www.kinopoisk.ru/film/988749/","https://www.kinopoisk.ru/film/5313869/"]



@dp.message(Command("films"))
async def cmd_name(message: Message):
    await message.answer("Выберите жанр", reply_markup=btn_keyboard)

@dp.message(lambda message: message.text == "Хоррор") 
async def show_horror(message: Message): 
    await message.reply("А вот и неплохой ужастик" + random.choice(horror)) 

@dp.message(lambda message: message.text == "Экшн") 
async def show_action(message: Message): 
    await message.reply("А вот и неплохой Экшн" + random.choice(action)) 

@dp.message(lambda message: message.text == "Фантастика") 
async def show_fantastic(message: Message): 
    await message.reply("А вот и неплохая фантастика" + random.choice(fantastic))    

@dp.message(lambda message: message.text == "Юмор") 
async def show_humor(message: Message): 
    await message.reply("А вот и неплохой Юмор" + random.choice(humor)) 

@dp.message(Command("start"))
async def cmd_name(message: Message):
    await message.answer("Привет, я тестовый бот")

@dp.message(Command("info"))
async def cmd_name(message: Message):
    await message.reply("У меня есть такие команды -\n /start, \n /info")

@dp.message(Command("name")) 
async def cmd_name(message: Message): 
    args = message.text.split(maxsplit=1) 
    if len(args) > 1: 
        await message.answer(f"Привет, <b>{args[1]}</b>", parse_mode="HTML") 
    else: 
        await message.answer("Пожалуйста, укажи своё имя после команды /name!") 

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

@dp.message(Command("test"))
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2") 



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



@dp.message(Command("weather")) 
async def start_command(message: Message): 
    await message.answer("Выберите город для погоды?"  ) 
 
@dp.message(F.text) 
async def get_weather(message:types.Message): 
    city = message.text 
    try: 
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347" 
        weather_data = requests.get(url).json() 
 
        temperature = weather_data["main"]["temp"] 
        temperature_feels =  weather_data["main"]["feels_like"] 
        wind_speed = weather_data['wind']['speed'] 
        cloud_cover = weather_data['weather'][0]['description'] 
        humidity = weather_data['main']['humidity'] 
 
        await message.answer(f"Температура воздуха: {temperature}\n" 
                             f"Ощущается как:{temperature_feels} \n" 
                             f"Ветер: {wind_speed} м/c \n " 
                             f"Облачность: {cloud_cover} \n" 
                             f"Влажность: {humidity}% ") 
    except KeyError: 
        await message.answer("Не удалось определить город"  ) 




# engine = pyttsx3.init() 
 
# engine.setProperty("rate",150) 
# engine.setProperty("volume",0.9) 
 
 
# engine.say("Добро пожаловать, как ваши дела?") 
# engine.say("что делали сегодня") 

# engine.runAndWait() 



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



