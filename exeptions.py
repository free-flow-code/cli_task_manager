from colorama import Fore, Style


class InvalidCommandException(Exception):
    def __init__(self, message="Не верная команда. Используйте 'main.py -h' для справки."):
        super().__init__(f"{Fore.RED}{message}{Style.RESET_ALL}")
