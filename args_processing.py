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
        "-c", "--command", choices=["view", "add", "edit", "find", "del"], help="Команда для выполнения."
    )
    parser.add_argument("--id", type=int, help="id задачи для изменения или удаления.")
    parser.add_argument("--name", type=str, help="Название задачи для изменения или удаления.")
    parser.add_argument(
        "--data", type=str, help="Данные для добавления или изменения задачи. В виде json в строковом представлении."
    )
    parser.add_argument("--category", type=str, help="Название категории для поиска задач по категории.")
    parser.add_argument("--keyword", type=str, help="Ключевые слова для поиска задач.")
    parser.add_argument("--status", type=str, help="Статус задачи для поиска задач по их статусу.")
    return parser.parse_args()
