import sys
from models import Task
from constants import (
    ARGS_HANDLERS,
    MAIN_MENU_HANDLERS,
    CLI_MESSAGES
)
from utils import print_tasks, validate_data
from exeptions import InvalidCommandException


class BaseTaskHandler:
    def __init__(self, handlers: dict):
        """
        Инициализирует базовый класс с набором обработчиков.

        :param handlers: Словарь с командами и соответствующими методами.
        :type handlers: dict
        """
        self.handlers = handlers

    def execute_command(self, command: str, params: dict) -> None:
        """
        Запускает метод класса в зависимости от переданной команды.
        Если параметры присутствуют - передает их в соответствующий обработчик.
        Если нет - вызывает обработчик без параметров.

        :param command: Название команды.
        :type command: str
        :param params: Параметры команды.
        :type params: dict
        :return: None
        """
        try:
            if command in dir(self):  # Проверяем, есть ли метод в текущем объекте
                handler = getattr(self, command, None)
                if handler:
                    handler(params)
            else:
                raise InvalidCommandException(f"Команда '{command}' не найдена.")
        except TypeError:
            print(CLI_MESSAGES.get("incorrect_params"))
            return

    @staticmethod
    def view_task(params: dict) -> None:
        """
        Выводит в консоль задачу по ее названию или id.
        Либо выводит список всех задач, если задан соответствующий параметр.
        """
        task_name = params.get("name")
        task_id = str(params.get("id"))

        if task_name:
            if task_name == "all":
                tasks = Task.get_all_tasks()
                print_tasks(tasks)
                return
            else:
                task = Task.get_task_by_name(task_name)
                print(task)
        elif task_id:
            task = Task.get_task_by_id(task_id)
        else:
            print(CLI_MESSAGES.get("incorrect_task_index"))
            return

        if not task:
            print(CLI_MESSAGES.get("task_not_found"))
            return
        print_tasks(task)

    @staticmethod
    def add_task(params: dict) -> None:
        """Добавляет новую задачу."""
        data = validate_data(params.get("data"))
        if not data:
            return

        try:
            task = Task(**data)
        except ValueError as err:
            print(CLI_MESSAGES.get("task_already_exist").format(err=err))
            return

        print(CLI_MESSAGES.get("success_add_task"))
        print_tasks({task.id: task.task_data})

    @staticmethod
    def edit_task(params: dict) -> None:
        """Обновляет данные задачи по ее названию или id."""
        data = validate_data(params.get("data"), creating=False)
        if not data:
            return

        task_name = params.get("name")
        task_id = str(params.get("id"))

        if task_name:
            updated_data = Task.update_task_by_name(task_name, data)
        elif task_id:
            updated_data = Task.update_task_by_id(str(task_id), data)
        else:
            print(CLI_MESSAGES.get("incorrect_task_index"))
            return

        if not updated_data:
            print(CLI_MESSAGES.get("task_not_found"))
            return

        print(CLI_MESSAGES.get("success_update_task"))
        print(updated_data)
        print_tasks(updated_data)

    @staticmethod
    def find_task(params: dict) -> None:
        """Производит поиск задач по категории, ключевым словам в названии и статусу."""
        category = params.get("category")
        keyword = params.get("keyword")
        status = params.get("status")

        if category:
            tasks = Task.find_tasks_by_category(category)
        elif keyword:
            tasks = Task.find_tasks_by_keyword(keyword)
        elif status:
            tasks = Task.find_tasks_by_status(status)
        else:
            print(CLI_MESSAGES.get("incorrect_find_data"))
            return

        if not tasks:
            return
        print_tasks(tasks)

    @staticmethod
    def delete_task(params: dict) -> None:
        """Удаляет задачу по ее имени или id."""
        task_name = params.get("name")
        task_id = str(params.get("id"))

        if task_name:
            is_deleted = Task.delete_task_by_name(task_name)
        elif task_id:
            is_deleted = Task.delete_task_by_id(str(task_id))
        else:
            print(CLI_MESSAGES.get("incorrect_task_index"))
            return

        if is_deleted:
            print(CLI_MESSAGES.get("success_del_task"))
            return
        print(CLI_MESSAGES.get("task_not_found"))


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
