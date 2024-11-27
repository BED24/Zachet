from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Вставь сюда свой API-ключ от погодного сервиса
API_KEY = '150d14aкак06fc5374b52c9612d2a98a305'
CITY = 'Moscow'  # Укажи нужный город


@app.route('/weather')
def get_weather():
    # Запрос к API погоды
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru'

    response = requests.get(url)
    data = response.json()

    # Проверка на успешный ответ
    if response.status_code == 200:
        weather_info = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify(weather_info)
    else:
        return jsonify({'error': 'Не удалось получить данные о погоде.'}), 500


if __name__ == '__main__':
    app.run(debug=True)

