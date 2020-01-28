"""
1) пишем класс User, реализующий логику обработки данных о пользователе;
2) пишем класс LastSeenLog, с помощью которого будет осуществляться работа
    с временем визита пользователя на наш воображаемый ресурс;
3) данные о времени визита пользователя будем хранить в виде пары значений:
    идентификатор пользователя, дата и время последнего визита;
4) данные каждого из этих классов будем хранить в формате JSON в соответствующих файлах:
    persons.json и last_seen_log.json.
"""

import os, json, uuid


#Путь к файлу с данными
USER_DATA_FILE_PATH = 'data.json'
# путь к файлу с данными о времени последнего посещения пользователя
LOG_DATA_FILE_PATH = 'time_log.json'

class Users:
    """
    Класс реализует логику для работы с данными о пользователях
    """
    def __init__(self):
        self.users = self.read()

    def read(self):
        """
        Читаем JSON с диска
        :param self:
        :return: list user data
        """
        # проверяем наличие файла на диске
        if not os.path.exists(USER_DATA_FILE_PATH):
            # возвращаем пустой список, если файл еще не создан
            return []
        # открываем файл на чтение
        with open(USER_DATA_FILE_PATH, 'r', encoding='utf-8') as fb:
            # Загружаем документ
            users = json.load(fb)
        # возвращаем список пользователей
        return users

    def save(self):
        """
        Сохраняет список пользователей JSON файле на диск
        :param self:
        :return: save jason file
        """
        # Открываем файл на запись
        with open(USER_DATA_FILE_PATH, 'w',encoding='utf-8') as fb:
            # сохраняем список пользователей в JSON
            json.dump(self.users, fb)

    def find(self, name):
        """
        Ищет среди списка всех зарегистрированных пользователей пользователя
    с именем name и возвращает его идентификатор. Если пользователь не найден, возвращает None.
        :param self:
        :param name:
        :return: user id
        """
        for user in self.users:
            #проверяем совпадение имени
            if user['first_name'] == name:
                #если имя совпало, возвращаем идентификатор пользователя
                return user['id']

    def add_user(self, user_data):
        """
        Добавляет данные пользователя user_data в список всех пользователей и сохраняет обновленный список
        :param self:
        :param user_data:
        :return:
        """
        self.users.append(user_data)
        self.save()

def request_data():
    """
      Осуществляет взаимодействие с пользователем и
      обрабатывает пользовательский ввод
    :return:
    """
    print('Привет! Я запишу твои данные!')
    # запрашиваем у пользователя данные
    first_name = input('Введи своё имя: ')
    last_name = input('А теперь фамилию: ')
    email = input('Мне еще понадобится адрес твоей электронной почты: ')

    # генерируем идентификатор пользователя и сохраняем его строковое представление
    user_id = str(uuid.uuid4())

    # создаем словарь пользователя
    user = {
        'id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    #возвращаем нового пользователя
    return user

def main():
    """
     Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    :return:
    """
    users = Users()
    # просим пользователя выбрать режим
    mode = input('Выбери режим.\n1 - найти пользователя по имени\n2 - ввести данные нового пользователя\n')
    # проверяем режим
    if mode == '1':
        # выбран режим поиска, запускаем его
        name = input('Введи имя пользователя для поиска: ')
        user_id = users.find(name)
        if user_id:
            print('Найден пользователь с идентификатором: ', user_id)
        else:
            print('Такого пользователя нет.')
    elif mode == '2':
        user_data = request_data()
        # добавляем нового пользователя в список всех пользователей
        users.add_user(user_data)
        print('Спасибо, данные сохранены!')
    else:
        print('Некорректный режим:( ')




if __name__ == '__main__':
    main()