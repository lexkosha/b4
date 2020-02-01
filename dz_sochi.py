# Импортируем необходимые модули
import sqlalchemy as sa 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
1)Сколько всего зарегистрировано атлетов женщин?
2)Сколько всего зарегистрировано атлетов старше 30 лет?
3)Сколько атлетов мужчин старше 25 лет получили 2 и более золотых медали?
"""

DB_PATH = 'sqlite:///sochi_athletes.sqlite3'

# Базовый класс моделей таблиц
Base = declarative_base()


class User(Base):
    # Указываем имя таблицы
    __tablename__ = 'user'
    id = sa.Column(sa.INTEGER, primary_key=True)
    # Имя
    first_name = sa.Column(sa.TEXT)
    # Фамилия
    last_name = sa.Column(sa.TEXT)
    # Пол
    gender = sa.Column(sa.TEXT)
    # почта
    email = sa.Column(sa.TEXT)
    # Дата рождения
    birthdate = sa.Column(sa.TEXT)
    # рост
    height = sa.Column(sa.REAL)


class Athelete(Base):
    # Имя таблицы 
    __tablename__ = 'athelete'
    id = sa.Column(sa.INTEGER, primary_key=True)
    # Возраст
    age = sa.Column(sa.INTEGER)
    #День рождения 
    birthdate = sa.Column(sa.TEXT)
    # Пол
    gender = sa.Column(sa.TEXT)
    # Высота (рост)
    height = sa.Column(sa.REAL)
    #Имя 
    name = sa.Column(sa.TEXT)
    # Вес (масса)
    weight = sa.Column(sa.TEXT)
    # Золотые медали 
    gold_medals = sa.Column(sa.INTEGER)
    # Серебренные медали 
    silver_medals = sa.Column(sa.INTEGER)
    # Бронзовые медали
    bronze_medals = sa.Column(sa.INTEGER)
    # Всего медалий 
    total_medals = sa.Column(sa.INTEGER)
    # Спорт (вид спорта)
    sport = sa.Column(sa.TEXT)
    # Страна
    country = sa.Column(sa.TEXT)


# Создаем соединение к базе
engine = sa.create_engine(DB_PATH,echo=True)
# Создаем фабрику сессию
Sessions = sessionmaker(engine)
# Создаем сессию
session = Sessions()

user = session.query(User).all()


def main():
    """
    Логика вывода
    """
    atheletes = session.query(Athelete).all()
    intro = int(input('Введите цифру чтоб получить ответ \n\
    Сколько всего зарегистрировано атлетов женщин? = 1 \n\
    Сколько всего зарегистрировано атлетов старше 30 лет? = 2\n\
    Сколько атлетов мужчин старше 25 лет получили 2 и более золотых медали? = 3\n\
        введите ответ: '))
    if intro == 1:
        females = 0
        for item in atheletes:
            if item.gender == 'Female':
                females += 1
        print(f'Всего женщин атлетов: {females}')
    elif intro == 2:
        all_athlete = 0
        for i in atheletes:
            if i.age >= 31:
                all_athlete += 1
        print(f'Всего атлетов: {all_athlete}')
    elif intro == 3:
        mans = 0
        for i in atheletes:
            if i.age >= 26 and i.gender == 'Male' and i.gold_medals >= 2:
                mans += 1
        print(f'Всего мужчин >25 и более 2 медалей: {mans}')
        
#     females = []

        
# print(females, len(females))

if __name__ == "__main__":
    main()