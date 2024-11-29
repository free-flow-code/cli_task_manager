import sys
from colorama import init
from constants import (
    LOGO,
    MAIN_MENU,
    INPUT_ERROR,
    WAIT_COMMAND,
    MAIN_MENU_HANDLERS
)
from models import CliArgsHandler
from args_processing import parse_arguments
from exeptions import InvalidCommandException


def show_main_menu(logo: bool = True):
    menu = MAIN_MENU
    if logo:
        menu += LOGO
    print(menu)

    try:
        input_number = int(input(WAIT_COMMAND))
        if input_number not in MAIN_MENU_HANDLERS.keys():
            print(INPUT_ERROR)
            return show_main_menu(logo=False)

        main_handler(input_number)
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
        command = args.command

        if command is None:
            raise InvalidCommandException

        task_manager = CliArgsHandler()
        task_manager.execute_command(command, args.params)
    except InvalidCommandException as err:
        print(err)


if __name__ == '__main__':
    init(autoreset=True)
    main()
