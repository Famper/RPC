from random import choice
from .config_json import RPC_items


def computer_generate():
    return choice(list(RPC_items.keys()))


def enter_user_item():
    try:
        user_item = int(input('Введи цифру, которая означает один из 3-х предметов.'
                              '\n\n0: Камень\n1: Ножницы\n2: Бумага\n-1: Выйти\n'
                              '\n[USER]: '))

        if user_item == -1:
            exit(0)

        if RPC_items[user_item]:
            return user_item

        return enter_user_item()
    except ValueError:
        enter_user_item()


def who_win(user_key: int, computer_key: int):
    if user_key == computer_key:
        return "\nНичья"
    elif (user_key == 0 and computer_key == 1)\
            or (user_key == 1 and computer_key == 2)\
            or (user_key == 2 and computer_key == 0):
        return "\nПользователь победил"
    else:
        return "\nКомпьютер победил"
