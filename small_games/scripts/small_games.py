#!/usr/bin/env python3
from colorama import Fore
from small_games.cli import welcome_user


def greet():
    print(Fore.GREEN + 'Welcome to the Small Games!')

    welcome_user()


def main():
    greet()


if __name__ == '__main__':
    main()
