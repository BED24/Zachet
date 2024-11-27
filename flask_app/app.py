# библиотеки
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# подключения к базе данных PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",         # Адрес базы данных (обычно localhost)
        database="users", # Название базы данных
        user="postgres",         # Ваш пользователь базы данных
        password="DB_PASSWORD"  # Ваш пароль базы данных
    )
    return conn


@app.route('/')
def home():
    return "Добро пожаловать на мой сайт!"

# регистрации
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']

    # Подключаемся к базе данных
    conn = get_db_connection()
    cur = conn.cursor()

    # Добавление нового пользователя в таблицу
    cur.execute(
        "INSERT INTO users (email, password, role) VALUES (%s, %s, %s)",
        (email, password, role)
    )
    conn.commit()

    # Закрытие соединения
    cur.close()
    conn.close()

    return jsonify({"message": "User registered successfully!"}), 200

# данных о погоде
@app.route('/weather', methods=['GET'])
def get_weather():
    # Пример данных
    weather_data = {
        "temperature": 22,
        "description": "Облачно",
        "humidity": 60,
        "wind_speed": 5
    }
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True, port=5000)



from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Настройка БАЗы
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",         # Адрес базы данных (обычно localhost)
        database="users",         # Название базы данных
        user="postgres",          # Ваш пользователь базы данных
        password="DB_PASSWORD"    # Ваш пароль базы данных
    )
    return conn


@app.route('/')
def home():
    return "Добро пожаловать на мой сайт!"


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']

    # Подключаемся к базе данных
    conn = get_db_connection()
    cur = conn.cursor()

    # Добавление нового пользователя в таблицу
    cur.execute(
        "INSERT INTO users (email, password, role) VALUES (%s, %s, %s)",
        (email, password, role)
    )
    conn.commit()


    cur.close()
    conn.close()

    return jsonify({"message": "User registered successfully!"}), 200

# добавления комментария
@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment_text = request.form['comment']  # Получаем текст комментария из формы

    # Если комментарий не пустой
    if comment_text:
        #
        conn = get_db_connection()
        cur = conn.cursor()


        cur.execute(
            "INSERT INTO comments (comment) VALUES (%s)",
            (comment_text,)
        )
        conn.commit()


        cur.close()
        conn.close()

        return jsonify({"message": "Комментарий успешно добавлен!"}), 200
    else:
        return jsonify({"error": "Комментарий не может быть пустым!"}), 400

# Пример получения данных о погоде
@app.route('/weather', methods=['GET'])
def get_weather():
    # Пример о погоде после нажатие кнопки...
    weather_data = {
        "temperature": 22,
        "description": "Облачно",
        "humidity": 60,
        "wind_speed": 5
    }
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=True)

