import sys
from models import Task
from constants import (
    ARGS_HANDLERS,
    MAIN_MENU_HANDLERS,
    CLI_MESSAGES
)
from utils import print_tasks
from exeptions import InvalidCommandException


class BaseTaskHandler:
    def __init__(self, handlers: dict):
        """
        Инициализирует базовый класс с набором обработчиков.

        :param handlers: Словарь с командами и соответствующими методами.
        :type handlers: dict
        """
        self.handlers = handlers

    def execute_command(self, command: str, params: dict = None) -> None:
        """
        Запускает метод класса в зависимости от переданной команды.
        Если параметры присутствуют - передает их в соответствующий обработчик.
        Если нет - вызывает обработчик без параметров.

        :param command: Название команды.
        :type command: str
        :param params: Параметры команды.
        :type params: list
        :return: None
        """
        if command in dir(self):  # Проверяем, есть ли метод в текущем объекте
            handler = getattr(self, command, None)
            if handler:
                handler(params)
        else:
            raise InvalidCommandException(f"Команда '{command}' не найдена.")

    @staticmethod
    def view_task(params: dict) -> None:
        """
        Выводит в консоль задачу по ее названию или id.
        Либо выводит список всех задач, если задан соответствующий параметр.
        """
        task_name = params.get("name")
        task_id = str(params.get("id"))
        tasks = None
        if task_name:
            if task_name == "all":
                tasks = Task.get_all_tasks()
            else:
                task = Task.get_task_by_name(task_name)
                tasks = {task.id: task.task_data} if task else None
        elif task_id:
            task = Task.get_task_by_id(task_id)
            tasks = {task_id: task.task_data} if task else None
        else:
            print(CLI_MESSAGES.get("incorrect_task_name"))
        if not tasks:
            print(CLI_MESSAGES.get("task_not_found"))
            return
        print_tasks(tasks)

    @staticmethod
    def edit_task(params: dict):
        pass

    def find_task(self, params: list[str]):
        pass

    def delete_task(self, params: list[str]):
        pass


class CliArgsHandler(BaseTaskHandler):
    def __init__(self):
        super().__init__(handlers=ARGS_HANDLERS)


class CliMenuHandler(BaseTaskHandler):
    def __init__(self):
        super().__init__(handlers=MAIN_MENU_HANDLERS)

    def show_view_task_menu(self):
        pass

    def show_add_task_menu(self):
        pass

    def show_edit_task_menu(self):
        pass

    def show_find_task_menu(self):
        pass

    def show_delete_task_menu(self):
        pass

    def exit(self):
        sys.exit()
