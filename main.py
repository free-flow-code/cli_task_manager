import sys
from colorama import init
from constants import (
    LOGO,
    MAIN_MENU,
    INPUT_ERROR,
    WAIT_COMMAND,
    ARGS_HANDLERS,
    MAIN_MENU_HANDLERS
)
from handlers import CliArgsHandler, CliMenuHandler
from args_processing import parse_arguments
from exeptions import InvalidCommandException


def show_main_menu(logo: bool = True):
    menu = MAIN_MENU
    if logo:
        menu = LOGO + menu
    print(menu)

    try:
        input_number = int(input(WAIT_COMMAND))
        if input_number not in MAIN_MENU_HANDLERS.keys():
            print(INPUT_ERROR)
            return show_main_menu(logo=False)

        menu_handler = CliMenuHandler()
        command = MAIN_MENU_HANDLERS[input_number]
        menu_handler.execute_command(command)
    except ValueError:
        print(INPUT_ERROR)
        return show_main_menu(logo=False)


def main():
    arguments = sys.argv[1:]
    if not arguments:
        show_main_menu()
        return

    try:
        args = parse_arguments()
        action = args.command

        if action is None:
            raise InvalidCommandException

        args_handler = CliArgsHandler()
        command = ARGS_HANDLERS[action]
        args_handler.execute_command(command, vars(args))
    except Exception as err:
        print(err)


if __name__ == '__main__':
    init(autoreset=True)
    main()
