import sqlite3
import datetime


def change_user_model(model, player_id):
    query = f"""UPDATE user_settings 
                SET model = '{model}'
                WHERE user_id = '{player_id}'"""
    connection = sqlite3.connect("db/game.db")
    cursor = connection.cursor()
    cursor.execute(query).fetchall()
    connection.commit()
    connection.close()


def get_user_id(login, password):
    query = f"SELECT id FROM users WHERE login = '{login}' AND password = '{password}'"
    connection = sqlite3.connect("db/game.db")
    cursor = connection.cursor()
    res = cursor.execute(query).fetchall()
    connection.close()
    return res[0][0]


def change_selected_user(user_id):
    query = f"""UPDATE selected_user 
                SET user_id = '{user_id}' 
                WHERE id = '1'"""
    connection = sqlite3.connect("db/game.db")
    cursor = connection.cursor()
    cursor.execute(query).fetchall()
    connection.commit()
    connection.close()


def this_uniqe_login(login):
    query = f"SELECT id FROM users WHERE login = '{login}'"
    connection = sqlite3.connect("db/game.db")
    cursor = connection.cursor()
    user_id = cursor.execute(query).fetchone()
    if user_id:
        return False
    else:
        return True


def add_new_user(login, password):
    query = f"INSERT INTO users (login, password) VALUES ('{login}', '{password}')"
    try:
        connection = sqlite3.connect("db/game.db")
        cursor = connection.cursor()
        cursor.execute(query).fetchall()
        connection.commit()
        user_id = get_user_id(login, password)
        query = f"INSERT INTO user_settings (user_id, model) VALUES ('{user_id}', '1')"
        cursor.execute(query).fetchall()
        connection.commit()
        connection.close()
        return True
    except Exception:
        return False


def get_selected_user():
    query = f"SELECT user_id FROM selected_user WHERE id = 1"
    connection = sqlite3.connect("db/game.db")
    cursor = connection.cursor()
    user_id = cursor.execute(query).fetchall()
    connection.close()
    return user_id[0][0]


def get_user_model(user_id):
    query = f"""SELECT img_player
                 FROM models
                 WHERE id = (
                             SELECT model
                             FROM user_settings
                             WHERE user_id = '{user_id}')"""

    connection = sqlite3.connect("db/game.db")
    cursor = connection.cursor()
    user_model = cursor.execute(query).fetchall()
    connection.close()
    return user_model[0][0]


def new_score(user_id, score):
    now_dt = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
    query = f"INSERT INTO records (user_id, score, date) VALUES('{user_id}', '{score}', '{now_dt}')"
    connection = sqlite3.connect("db/game.db")
    cursor = connection.cursor()
    cursor.execute(query).fetchall()
    connection.commit()
    connection.close()


def get_all_score():
    query = f"""SELECT DISTINCT    users.login,
                                   score, date
                              FROM records
                                   FULL OUTER JOIN
                                   users ON records.user_id = users.id
                             WHERE score > 0
                             ORDER BY score desc, date desc
                             LIMIT 10"""
    connection = sqlite3.connect("db/game.db")
    cursor = connection.cursor()
    all_score = cursor.execute(query).fetchall()
    connection.close()
    return list(map(lambda x: f'Логин: {x[0]} Результат: {x[1]} Дата: {x[2]}', all_score))
