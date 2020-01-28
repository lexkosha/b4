import os, json, uuid

DATA_FILE_PATH = 'data.json'

def read():
    """
    Читаем файл с данными с диска
    :return: users
    """
    #Проверим создан ли файл на диске
    if not os.path.exists(DATA_FILE_PATH):
        # вернем пустой список если файл не создан
        return []

    #Открываем файл на чтение
    with open(DATA_FILE_PATH) as fb:
        users = json.load(fb)

    return users

def save(users):
    """
      Сохраняет список пользователей users в JSON файле на диск

    :param users: принимаем json с данными
    :return: сохраняем файл с данными
    """
    with open(DATA_FILE_PATH, 'w', encoding='UTF-8') as fb:
        json.dump(users, fb)



def find(users):
    """
    Ищет среди списка пользователей users пользователя с заданным именем
    и возвращает его идентификатор. Если пользователь не найден, возвращает None.
    :param users:
    :return:
    """
    name = input('Ведите имя пользователя для поиска: ')
    for user in users:
        # проверяем совпадение имени
        if user['first_name'] == name:
            # если имя совпало, возвращаем идентификатор пользователя
            return user['id']

def valid_email(email):
    """
      Проверяет наличие хотя бы одной точки в домене и знака @ в email.
      Возвращает True, если email допустимый и False - в противном случае.
    :param email:
    :return:
    """
    if '.' and '@' in email['email']:
        return True
    else:
        return False




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
    # читаем список сохранённых пользователей
    user_list = read()

    # просим пользователя выбрать режим
    mode = input('Выбери режим.\n1 - найти пользователя по имени\n2 - ввести данные нового пользователя\n')
    if mode == '1':
    # выбран режим поиска, запускаем его
        user_id = find(user_list)

        if user_id:
            print('Найден пользователь с идентификатором: ', user_id)
        else:
            print('Такого пользователя нет!')
    elif mode == '2':
        user = request_data()
        check_mail = valid_email(user)
        if check_mail == True:
            # добавляем нового пользователя в список всех пользователей
            user_list.append(user)
            # сохраняем список пользователей
            save(user_list)
            print('Спасибо данные сохранены!')
        elif check_mail == False:
            print('Вы ввели не корректный email, попробуйте снова!')

        else:
            print('Ошибка в проверки валидации email адреса')

    else:
        print('Не корректный режим')

if __name__ == '__main__':
    main()
