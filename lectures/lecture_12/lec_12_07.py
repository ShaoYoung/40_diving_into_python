# ООП. Финал.
# Менеджер контекста with

import sqlite3


class DB:
    def __init__(self, name):
        # name - имя файла с БД
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        # создание connection и cursor
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor

    # агрументы обязательны на случай ошибки во время работы кода внутри менеджера контекста
    # exc_type - тип ошибки, exc_val - значение ошибки, трассировка
    # если ошибки не было, все три аргумента - None
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


db = DB('sqlite.db')
with db as cur:
    cur.execute("""create table if not exists users(name,age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")

with db as cur:
    cur.execute("""insert into users values ('Хуанита', 25);""")

