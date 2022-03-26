import prompt
from colorama import Fore


def welcome_user():
    name = prompt.string(Fore.GREEN + 'May I have your name? ')
    print(Fore.GREEN + 'Hello, {}!'.format(name))
