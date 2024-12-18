import asyncio 
import logging 
from aiogram import Bot, Dispatcher, types,F 
from aiogram.filters import Command 
from aiogram.types import Message 
import requests 
import pyttsx3 

logging.basicConfig(level=logging.INFO) 
bot = Bot(token="7869107441:AAFQtwknik44NcV2_p3fJBZmwKIcyUjX5QA") 
dp = Dispatcher() 
@dp.message(Command("start")) 
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
 
@dp.message(Command("help")) 
async def cmd_start(message: types.Message): 
    await message.reply("Тут помощь") 

@dp.message(lambda message: message.text == "Запросить викторину")
async def send_quiz(message: types.Message):
    question = "Какой самый большой океан на Земле?"
    options = ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"]
    correct_option_id = 2  # Правильный вариант ответа (начиная с 0)
    
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type='quiz',
        correct_option_id=correct_option_id,
        is_anonymous=False  # Убираем анонимность
    )


@dp.message(Command("special_buttons")) 
async def cmd_special_buttons(message: types.Message): 
    kb = [
        [types.KeyboardButton(text="Запросить геолокацию", request_location=True)],
        [types.KeyboardButton(text="Запросить контакт", request_contact=True)],
        [types.KeyboardButton(text="Запросить викторину", request_poll=types.KeyboardButtonPollType(type='quiz'))],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)  
    await message.reply("Выберите действие", reply_markup=keyboard)



# @dp.message() 
# async def cmd_start(message: Message): 
#     await message.answer(message.text) 


@dp.message(Command("name")) 
async def cmd_name(message: Message): 
    args = message.text.split(maxsplit=1) 
    if len(args) > 1: 
        await message.answer(f"Привет, <b>{args[1]}</b>", parse_mode="HTML") 
    else: 
        await message.answer("Пожалуйста, укажи своё имя после команды /name!") 
 
@dp.message(Command("weather")) 
async def start_command(message:types.Message): 
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
        pass 
    except KeyError: 
        await message.answer("Не удалось определить город"  ) 
 
 

# engine = pyttsx3.init() 
 
# engine.setProperty("rate",150) 
# engine.setProperty("volume",0.9) 
 
 
# engine.say("ПРивет всем еще раз") 
# engine.say("Hello everyone") 
# engine.runAndWait() 
 
async def main(): 
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot) 
 
if __name__ == "__main__": 
    asyncio.run(main())