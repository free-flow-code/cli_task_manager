import sys
from colorama import init
from constants import LOGO, MAIN_MENU, WAIT_COMMAND
from models import TaskManager
from args_processing import parse_arguments
from exeptions import InvalidCommandException


def show_main_menu():
    print(LOGO, MAIN_MENU)
    command_number = input(WAIT_COMMAND)


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

        task_manager = TaskManager()
        task_manager.execute_command(command, args.params)
    except InvalidCommandException as err:
        print(err)


if __name__ == '__main__':
    init(autoreset=True)
    main()
