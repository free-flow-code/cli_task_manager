import argparse
import textwrap


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="Cli Task Manager",
        description=textwrap.dedent(
            """
            Application for managing a task list with the ability to add, complete, delete and search for tasks.
            """
        )
    )
    # Просмотр задач
    parser.add_argument(
        "-tl", "--task-list", action="store_true", help="View the list of tasks."
    )
    parser.add_argument(
        "-t", "--task", nargs=1, type=str, help="View task by name."
    )
    parser.add_argument(
        "-cl", "--category-list", action="store_true", help="View the list of categories."
    )
    parser.add_argument(
        "-c", "--category", nargs=1, type=str, help="View the list of task categories."
    )
    # Добавление задачи
    # Изменение задачи
    # Удаление задачи
    # Поиск задач
