import sys
from constants import LOGO, MAIN_MENU
from models import TaskManager
from args_processing import parse_arguments


def show_main_menu():
    print(LOGO, MAIN_MENU)
    command_number = input("Ожидание ввода: ")


def main():
    arguments = sys.argv[1:]
    if not arguments:
        show_main_menu()
        return

    try:
        args = parse_arguments()
        task_manager = TaskManager()
        task_manager.execute_command(args)
    except SystemExit:
        print(f"Invalid arguments provided!")
        return


if __name__ == '__main__':
    main()
