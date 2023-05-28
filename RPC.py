from config.config_json import RPC_items
from config.methods import (enter_user_item, computer_generate, who_win)


if __name__ == '__main__':
    while True:
        user = enter_user_item()
        print(f'\nВы выбрали: {RPC_items[user]}')
        computer = computer_generate()
        print(f'Компьютер выбрал: {RPC_items[computer]}')
        print(who_win(user, computer))

