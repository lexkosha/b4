def make_russian(number):
    if number == 1:
        return f'{number} студент'
    elif number == 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19:
        return f'{number} студентов'
    elif number % 10 == 0:
        return f'{number} студентов'
    elif number % 2 != 0:
        return f'{number} студента'
    elif number % 2 == 0:
        return f'{number} студента'
    
