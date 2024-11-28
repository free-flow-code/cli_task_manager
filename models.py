from datetime import date
from enum import Enum
from constants import HANDLERS, CATEGORIES_FILEPATH
from files_processing import open_json_file, save_to_json_file
from exeptions import InvalidCommandException


class Category:
    _categories = {}

    def __new__(cls, *args, filepath: str = CATEGORIES_FILEPATH):
        cls._categories = open_json_file(filepath)
        return super().__new__(cls)

    def __init__(self, name: str, task_id: int):
        self.name = name
        self.tasks: list = self._categories.get(name, [])
        if task_id not in self.tasks:
            self.tasks.append(task_id)
            self._categories[name] = self.tasks
            self._save_categories()

    @classmethod
    def add_task_to_category(cls, category_name: str, task_id: int) -> None:
        """
        Добавляет идентификатор задачу в категорию.

        :param category_name: Название категории, к которой добавляется задача.
        :type category_name: str
        :param task_id: Уникальный идентификатор задачи, добавляемой в категорию.
        :type task_id: int
        :return: None
        """
        if category_name in cls._categories:
            if task_id not in cls._categories[category_name]:
                cls._categories[category_name].append(task_id)
        else:
            cls._categories[category_name] = [task_id]
        cls._save_categories()

    @classmethod
    def _save_categories(cls, filepath: str = CATEGORIES_FILEPATH) -> None:
        """
        Сохраняет категории в json файл.

        :param filepath: Путь к файлу
        :type filepath: str
        :return: None
        """
        save_to_json_file(cls._categories, filepath)

    @classmethod
    def get_all_categories(cls) -> list:
        return list(cls._categories.keys())


class TaskPriority(Enum):
    low = "Низкий"
    middle = "Средний"
    high = "Высокий"


class TaskStatus(Enum):
    done = "Готова"
    not_done = "Не готова"


class Task:
    _tasks_count = 0

    def __new__(cls, *args, **kwargs):
        cls._tasks_count += 1
        return super.__new__(cls)

    def __init__(self, **kwargs):
        self.id: int = self._tasks_count - 1
        self.title: str = kwargs.get("title", "Без названия")
        self.description: str = kwargs.get("description", "")
        self.category: str = kwargs.get("category", "Общее")
        self.due_date: date = kwargs.get("due_date", date.today())
        self.priority: TaskPriority = kwargs.get("priority", TaskPriority.middle)
        self.status: TaskStatus = kwargs.get("status", TaskStatus.not_done)
        Category.add_task_to_category(self.category, self.id)


class TaskManager:
    def __init__(self):
        self.handlers: dict = HANDLERS

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
            handler = getattr(self, handler_name)
            if params:
                handler(params)
            else:
                handler()
        else:
            raise InvalidCommandException

    def view_task(self, params: list[str]):
        pass

    def edit_task(self, params: list[str]):
        pass

    def find_task(self, params: list[str]):
        pass

    def delete_task(self, params: list[str]):
        pass
