import re


def get_strength_point(match):
    return 1 if match else 0


def clicked(psw):
    password = psw
    strength_point = 0

    #long length
    strength_point += get_strength_point(len(password) > 8)

    # exist number
    strength_point += get_strength_point(re.search(r"\d", password))

    # exist big word
    strength_point += get_strength_point(re.search(r"[A-Z]", password))

    # exist small word
    strength_point += get_strength_point(re.search(r"[a-z]", password))

    # cool symbol
    strength_point += get_strength_point(re.search(r"\W", password))

    if 0 <= strength_point < 2:
        #'Легкий пароль'
        return 0
    elif 2 <= strength_point < 4:
        #'Средний пароль'
        return 1
    else:
        #'Сложный пароль'
        return 2
