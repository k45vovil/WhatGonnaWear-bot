import os
import time

from dotenv import load_dotenv
import requests
from requests.exceptions import RequestException
import telebot
from telebot import types


load_dotenv()
telegram_token = os.getenv('telegram_token')
weather_token = os.getenv('weather_token')

bot = telebot.TeleBot(telegram_token)
URL = 'http://api.openweathermap.org/data/2.5/forecast'


def get_weather(city):
    weather_parameters = {
            'q': city,
            'appid': weather_token,
            'units': 'metric',
            'lang': 'ua'
        }

    try:
        response = requests.get(url=URL, params=weather_parameters)

        temp = round(response.json()['list'][0]['main']['temp'])
        feels_like = round(response.json()['list'][0]['main']['feels_like'])
        humidity = response.json()['list'][0]['main']['humidity']
        description = response.json()['list'][0]['weather'][0]['description'].capitalize()
        wind_speed = round(response.json()['list'][0]['wind']['speed'])
        time = response.json()['list'][0]['dt_txt'].split(' ')[1].split(':')[0]

        if feels_like < -25:
            advice = '<b>Рекомендую</b>☝🏻: Краще сиди вдома умаляю... 🏠 Ну, чи дуже тепло одягайся!'
        elif -25 <= feels_like < -20:
            advice = '<b>Рекомендую</b>☝🏻: Не забудь про термобілизну! ❄️ Ппц зима лютая 🌨...'
        elif -20 <= feels_like < -15:
            advice = '<b>Рекомендую</b>☝🏻: Мсьє, діставай пуховик і тепле взуття ❄️'
        elif -15 <= feels_like < -10:
            advice = '<b>Рекомендую</b>☝🏻: Теплий шарф 🧣 та светр замінить кружку гарячої кави ☕️.'
        elif -10 <= feels_like < -5:
            advice = '<b>Рекомендую</b>☝🏻: Бррр зимно... 🧦 Не забудь рукавички та шапку!'
        elif -5 <= feels_like < 0:
            advice = '<b>Рекомендую</b>☝🏻: Тепла куртка та стільовий шарф сьогодні як ніколи до речі!🧣'
        elif 0 <= feels_like < 5:
            advice = '<b>Рекомендую</b>☝🏻: Улюблений світшот чи теплий спортивний костюм не дадуть замерзнути дупі🍑'
        elif 5 <= feels_like < 10:
            advice = '<b>Рекомендую</b>☝🏻: Ну дуууже легенька курточка тобі сьогодні не завадить💁'
        elif 10 <= feels_like < 15:
            advice = '<b>Рекомендую</b>☝🏻: Вигулюємо нові кроси 👟 та худі'
        elif 15 <= feels_like < 20:
            advice = '<b>Рекомендую</b>☝🏻: Знімай нафіг верхній одяг! Час спортивок 👕 та кофт'
        elif 20 <= feels_like < 25:
            advice = '<b>Рекомендую</b>☝🏻: Сьогодні шортики 🩳 та майка - пощебече твої яйка!'
        elif 25 <= feels_like:
            advice = '<b>Рекомендую</b>☝🏻: Мінімум шмоток - максимум засмаги, кабанчик 🌞🏖'

        res = f'{advice}\n\n📍Погода у - м. <b>{city}</b> в {time}:00\n{description}.'
            res = f'🌡<i>Температура повітря:</i> {temp}°C, <i>відчувається як:</i> {feels_like}°C. 💧<i>Вологість:</i> {humidity} %, 🌬<i>швидкість вітру</i> {wind_speed} м/с.'

        temp2 = round(response.json()['list'][2]['main']['temp'])
        feels_like2 = round(response.json()['list'][2]['main']['feels_like'])
        humidity2 = response.json()['list'][2]['main']['humidity']
        description2 = response.json()['list'][2]['weather'][0]['description'].capitalize()
        wind_speed2 = round(response.json()['list'][2]['wind']['speed'])
        time2 = response.json()['list'][2]['dt_txt'].split(' ')[1].split(':')[0]
        res2 = f'📍Погода у - м. <b>{city}</b> в {time2}:00\n{description2}. 🌡<i>Температура повітря:</i> {temp2}°C, <i>відчувається як:</i> {feels_like2}°C. 💧<i>Вологість:</i> {humidity2} %, 🌬<i>швидкість вітру</i> {wind_speed2} м/с.'

        temp3 = round(response.json()['list'][4]['main']['temp'])
        feels_like3 = round(response.json()['list'][4]['main']['feels_like'])
        humidity3 = response.json()['list'][4]['main']['humidity']
        description3 = response.json()['list'][4]['weather'][0]['description'].capitalize()
        wind_speed3 = round(response.json()['list'][4]['wind']['speed'])
        time3 = response.json()['list'][4]['dt_txt'].split(' ')[1].split(':')[0]
        res3 = f'📍Погода у - м. <b>{city}</b> в {time3}:00\n{description3}. 🌡<i>Температура повітря:</i> {temp3}°C, <i>відчувається як:</i> {feels_like3}°C. 💧<i>Вологість:</i> {humidity3} %, 🌬<i>швидкість вітру</i> {wind_speed3} м/с.'

        final_message = f'{res}\n\n{res2}\n\n{res3}'
    except KeyError:
        final_message = 'Чесно, я шукав! 🥺 Але такого міста незнаю 😔'
    except RequestException:
        final_message = 'Щось пішло не так...🤮'

    return final_message


def main():

    while True:
        try:
            @bot.message_handler(commands=['start'])
            def start(message):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton('Цумань')
                btn2 = types.KeyboardButton('Луцьк')
                btn3 = types.KeyboardButton('Рівне')
                btn4 = types.KeyboardButton('Львів')
                btn5 = types.KeyboardButton('Київ')
                btn6 = types.KeyboardButton('Світязь')
                btn7 = types.KeyboardButton('Дніпро')
                btn8 = types.KeyboardButton('Одеса')
                markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                text = f'<b>Здрасьтє 🤚, {message.from_user.first_name}!</b>\nНапиши назву міста або вибери зі списку. Я надішлю тобі прогноз погоди ☂️'
                bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)

            @bot.message_handler(content_types=['text'])
            def mess(message):
                final_message = get_weather(message.text)
                bot.send_message(message.chat.id, final_message, parse_mode='html')

            bot.polling(none_stop=True)

        except KeyboardInterrupt:
            finish = input(
                'Вы действительно хотите прервать работу бота? Y/N: '
                )
            if finish in ('Y', 'y'):
                print('До встречи!')        
            elif finish in ('N', 'n'):
                print('Продолжаем работать!')

        except Exception as e:
            print(f'Бот упал с ошибкой: {e}')
            time.sleep(5)


if __name__ == '__main__':
    main()
