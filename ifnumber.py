def make_russian(number):
    if number == 1:
        return f'{number} студент'
    elif number % 10 == 0:
        return f'{number} студентов'
    elif number % 2 != 0:
        return f'{number} студента'
    elif number % 2 == 0:
        return f'{number} студента'
