from argparse import Namespace
from constants import HANDLERS


class TaskManager:
    def __init__(self):
        self.handlers: dict = HANDLERS

    def execute_command(self, args: Namespace) -> None:
        """
        Запускает метод класса в зависимости от переданного аргумента командной строки.
        Если аргумент присутствует и не является булевым, передает его в соответствующий обработчик.
        Если аргумент булевый или отсутствует, вызывает обработчик без параметров.

        :param args: Объект с аргументами командной строки, полученный через argparse.
        :type args: Namespace
        :return: None
        """
        for arg_name, handler_name in self.handlers.items():
            if getattr(args, arg_name):
                handler = getattr(self, handler_name)
                args_value = vars(args).get(f"{arg_name}")

                if args_value and not isinstance(args_value, bool):
                    handler(args_value)
                else:
                    handler()
                break

    def view_task_list(self):
        print("Просмотр списка задач")

    def view_task_by_name(self, task_name: list[str]):
        print(f"Просмотр задачи {task_name}")

    def view_category_list(self):
        print("Просмотр списка категорий")

    def view_tasks_by_category(self, category_name: list[str]):
        print("Просмотр задач в категории")
