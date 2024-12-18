import asyncio
import logging
from aiogram import Bot, Dispatcher,types,F
from aiogram.filters import Command
from aiogram.types import Message
import requests 
from random import choice
import yt_dlp
import os
import time
from aiogram.types import InputFile
import requests 
import pyttsx3 


logging.basicConfig(level=logging.INFO)
bot = Bot(token='7869107441:AAFQtwknik44NcV2_p3fJBZmwKIcyUjX5QA')
dp = Dispatcher()

# Флаг для отслеживания запросов
waiting_for_weather = {}
waiting_for_response = {}

@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("У меня есть команда /start, /info, /button, /name, /weather и другие.")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет, я тестовый бот")

@dp.message(Command("movie"))
async def cmd_movie(message: Message):
    genres = [
        ("Комедия", "https://kinobar.my/komedii/"),
        ("Драма", "https://kinobar.my/dramy/"),
        ("Боевик", "https://kinobar.my/boeviki/"),
        ("Фантастика", "https://kinobar.my/fantastika/"),
        ("Ужасы", "https://kinobar.my/uzhasyy/"),
    ]

    # Создание кнопок с жанрами
    buttons = [
        [types.InlineKeyboardButton(text=genre[0], url=genre[1])] for genre in genres
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer("Выберите жанр фильма:", reply_markup=keyboard)
# Словарь с треками для каждого жанра
music_library = {
    "Поп": [
        "Dua Lipa - Levitating ffff",
        "The Weeknd - Blinding Lights",
        "Ava Max - Sweet but Psycho",
        "Ed Sheeran - Shivers",
        "Taylor Swift - Anti-Hero"
    ],
    "Рок": [
        "Queen - Bohemian Rhapsody",
        "Nirvana - Smells Like Teen Spirit",
        "Led Zeppelin - Stairway to Heaven",
        "Linkin Park - Numb",
        "Metallica - Enter Sandman"
    ],
    "Хип-хоп": [
        "Drake - God's Plan",
        "Eminem - Lose Yourself",
        "Kanye West - Stronger",
        "Kendrick Lamar - Humble",
        "Post Malone - Circles"
    ],
    "Джаз": [
        "Miles Davis - So What",
        "Louis Armstrong - What a Wonderful World",
        "Norah Jones - Don't Know Why",
        "John Coltrane - Giant Steps",
        "Diana Krall - The Look of Love"
    ],
    "Электронная музыка": [
        "David Guetta - Titanium",
        "Avicii - Wake Me Up",
        "Calvin Harris - Summer",
        "Deadmau5 - Strobe",
        "Marshmello - Alone"
    ]
}

# Хранилище для уникальных треков по пользователям
user_music_sessions = {}

@dp.message(Command("music"))
async def cmd_music(message: Message):
    genres = list(music_library.keys())

    # Создание кнопок с жанрами
    buttons = [
        [types.InlineKeyboardButton(text=genre, callback_data=f"genre_{genre}")]
        for genre in genres
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer("Выберите жанр музыки:", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith("genre_"))
async def select_genre(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    genre = callback_query.data.split("_")[1]

    # Получаем список треков для жанра
    available_tracks = music_library[genre]

    # Проверяем, если у пользователя уже были предложены треки
    if user_id not in user_music_sessions:
        user_music_sessions[user_id] = {}

    user_genre_tracks = user_music_sessions[user_id].get(genre, [])
    remaining_tracks = [track for track in available_tracks if track not in user_genre_tracks]

    # Если все треки уже были показаны, сбрасываем список
    if not remaining_tracks:
        user_genre_tracks = []
        remaining_tracks = available_tracks

    # Выбираем случайный трек
    selected_tracks = [choice(remaining_tracks) for _ in range(3)]

    # Обновляем историю пользователя
    user_music_sessions[user_id][genre] = user_genre_tracks + selected_tracks

    # Отправляем треки пользователю
    await callback_query.message.answer(f"Вот треки для жанра {genre}:\n" +
                                        "\n".join(f"- {track}" for track in selected_tracks))

    await callback_query.answer()

@dp.message(Command("button"))
async def cmd_button(message: Message):
    kb = [
        [types.KeyboardButton(text="Первая кнопка")],
        [types.KeyboardButton(text="Вторая кнопка")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Какую кнопку вы выбрали?", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Первая кнопка")
async def first_btn(message: Message):
    await message.reply("Вы нажали на первую кнопку")

@dp.message(lambda message: message.text == "Вторая кнопка")
async def second_btn(message: Message):
    await message.reply("Вы нажали на вторую кнопку")

@dp.message(Command("name"))
async def cmd_name(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        await message.answer(f"Привет, <b>{args[1]}</b>", parse_mode="HTML")
    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")

@dp.message(Command("weather"))
async def start_command(message: types.Message):
    await message.answer("Выберите город для погоды?")
    # Устанавливаем флаг ожидания города
    waiting_for_weather[message.from_user.id] = True

@dp.message(F.text)
async def get_weather(message: types.Message):
    # Проверяем, ждет ли бот город для погоды
    if waiting_for_weather.get(message.from_user.id):
        city = message.text
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=your_api_key"
            weather_data = requests.get(url).json()

            temperature = weather_data["main"]["temp"]
            temperature_feels = weather_data["main"]["feels_like"]
            wind_speed = weather_data['wind']['speed']
            cloud_cover = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']

            await message.answer(f"Температура воздуха: {temperature}°C\n"
                                 f"Ощущается как: {temperature_feels}°C\n"
                                 f"Ветер: {wind_speed} м/с\n"
                                 f"Облачность: {cloud_cover}\n"
                                 f"Влажность: {humidity}%")
        except KeyError:
            await message.answer("Не удалось определить город.")
        
        # Сбрасываем флаг ожидания
        waiting_for_weather[message.from_user.id] = False

    else:
        # Обработка текстового настроения, если это не запрос на погоду
        await analyze_mood(message)

@dp.message(F.animation)
async def echo_gif(message: types.Message):
    await message.reply_animation(message.animation.file_id)



async def analyze_mood(message: types.Message):
    text = message.text.lower()
    
    # Ключевые слова для анализа настроения
    if any(word in text for word in ["грустно", "плохое настроение", "развесели", "давай", "Мне грустно", "мне грустно"]):
        # Список рекомендаций для плохого настроения
        recommendations = [
            "Попробуй посмотреть комедию, например, 'Назад в будущее'!",
            "Вот шутка: Почему программисты не играют в прятки? Потому что им нельзя скрывать ошибки!",
            "Знаешь, когда мне грустно, я думаю о котиках! 🐱 Посмотри картинки с котиками — это помогает!",
        ]
        response = choice(recommendations)
        await message.answer(response)
    
    else:
        await message.answer("Я пока не понимаю, что ты имеешь в виду. Но могу рассказать шутку или что-то мотивирующее, если хочешь! Напиши 'давай', и я расскажу.")
        waiting_for_response[message.from_user.id] = True

@dp.message(lambda message: message.text.lower() == "давай")
async def tell_joke_or_motivation(message: types.Message):
    if waiting_for_response.get(message.from_user.id):
        jokes = [
            "Почему программисты не играют в футбол? Потому что не могут найти ворота!",
            "Какой любимый напиток у программистов? Чай, потому что он бесконечный!",
            "Сколько программистов нужно, чтобы поменять лампочку? Ни одного — это проблема оборудования!",
            "Программист идет в бар. Заказывает 'один коктейль'. Бармен говорит: 'Я не знаю, что это.' Программист отвечает: 'Тогда ошибку мне в стек.'",
            "Почему Java-программисты носят очки? Потому что не видят C#!"
        ]
        
        motivations = [
            "Не важно, насколько медленно ты идешь, главное — не останавливаться!",
            "Помни, каждый шаг вперед приближает тебя к цели, даже если он кажется маленьким.",
        ]
        
        all_responses = jokes + motivations
        response = choice(all_responses)
        await message.answer(response)
        
        waiting_for_response[message.from_user.id] = False
    else:
        await message.answer("Напиши, если хочешь услышать шутку или получить немного мотивации!")



engine = pyttsx3.init() 
 
engine.setProperty("rate",150) 
engine.setProperty("volume",0.9) 
 
 
engine.say("Добро пожаловать, как ваши дела?") 

engine.runAndWait() 
 
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
