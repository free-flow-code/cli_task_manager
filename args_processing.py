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
    parser.add_argument("-p", "--params", nargs="*", help="Параметры команды.")
    return parser.parse_args()
