import argparse
import textwrap


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="TASKY - Cli Task Manager",
        description=textwrap.dedent(
            """
            Приложение для управления списком задач с возможностью добавления, завершения, удаления и поиска задач.
            """
        )
    )
    parser.add_argument(
        "-c", "--command", choices=["view", "add", "edit", "find", "delete"], help="Команда для выполнения."
    )
    parser.add_argument("--id", type=int, help="Параметры команды.")
    parser.add_argument("--name", type=str, help="Параметры команды.")
    parser.add_argument("--data", type=str, help="Параметры команды.")
    #parser.add_argument("params", nargs="*", help="Параметры команды.")
    return parser.parse_args()
