import sys
from constants import ARGS_HANDLERS, MAIN_MENU_HANDLERS
from exeptions import InvalidCommandException


class BaseTaskHandler:
    def __init__(self, handlers: dict):
        """
        Инициализирует базовый класс с набором обработчиков.

        :param handlers: Словарь с командами и соответствующими методами.
        :type handlers: dict
        """
        self.handlers = handlers

    def execute_command(self, command: str, params: list) -> None:
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
        handler_name = self.handlers.get(command)
        if handler_name:
            handler = getattr(self, handler_name, None)
            if handler:
                if params:
                    handler(params)
                else:
                    handler()
            else:
                raise AttributeError(f"Обработчик '{handler_name}' не найден в классе {self.__class__.__name__}.")
        else:
            raise InvalidCommandException(f"Команда '{command}' не найдена.")

    def view_task(self, params: list[str]):
        pass

    def edit_task(self, params: list[str]):
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
