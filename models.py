from enum import Enum
from datetime import date
from typing import Dict, List
from constants import HANDLERS, CATEGORIES_FILEPATH, TASKS_FILEPATH
from files_processing import open_json_file, save_to_json_file
from exeptions import InvalidCommandException


class Category:
    _filepath: str = CATEGORIES_FILEPATH
    _categories: Dict[str, List[int]] = open_json_file(_filepath)

    def __init__(self, name: str, task_id: int):
        self.name = name
        self.task_ids = self._add_task_id(task_id)
        self._save_to_file()

    def _add_task_id(self, task_id: int) -> List[int]:
        """Добавляет task_id в категорию."""
        if self.name in self._categories:
            if task_id not in self._categories[self.name]:
                self._categories[self.name].append(task_id)
        else:
            self._categories[self.name] = [task_id]
        return self._categories[self.name]

    def _save_to_file(self) -> None:
        """Сохраняет все категории в файл."""
        save_to_json_file(self._categories, self._filepath)

    @property
    def task_ids(self) -> List[int]:
        """Возвращает список задач категории."""
        return self._categories.get(self.name, [])

    @task_ids.setter
    def task_ids(self, task_ids: List[int]):
        """Устанавливает список задач категории и сохраняет изменения."""
        self._categories[self.name] = task_ids
        self._save_to_file()

    @classmethod
    def get_all_categories(cls) -> dict:
        """Возвращает реестр всех категорий."""
        return cls._categories


class TaskPriority(Enum):
    low = "Низкий"
    middle = "Средний"
    high = "Высокий"


class TaskStatus(Enum):
    done = "Готова"
    not_done = "Не готова"


class Task:
    _filepath: str = TASKS_FILEPATH
    _tasks: Dict[str, Dict] = open_json_file(_filepath)
    _tasks_count: int = len(_tasks)

    def __new__(cls, *args, **kwargs):
        cls._tasks_count += 1
        return super().__new__(cls)

    def __init__(self, **kwargs):
        self.id: str = kwargs.get("id", str(self._tasks_count + 1))
        self.title: str = kwargs.get("title", "Без названия")
        self.description: str = kwargs.get("description", "")
        self.category: str = kwargs.get("category", "Общее")
        self.due_date: date = kwargs.get("due_date", date.today())
        self.priority: TaskPriority = kwargs.get("priority", TaskPriority.middle)
        self.status: TaskStatus = kwargs.get("status", TaskStatus.not_done)
        self.priority: TaskPriority = (
            kwargs.get("priority")
            if isinstance(kwargs.get("priority"), TaskPriority)
            else TaskPriority(kwargs.get("priority", TaskPriority.middle.value))
        )
        self.status: TaskStatus = (
            kwargs.get("status")
            if isinstance(kwargs.get("status"), TaskStatus)
            else TaskStatus(kwargs.get("status", TaskStatus.not_done.value))
        )
        Category(self.category, int(self.id))

        # Добавляем задачу в общий реестр задач
        self._tasks[self.id] = {
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date.isoformat(),
            "priority": self.priority.value,
            "status": self.status.value,
        }
        self._save_to_file()

    def _save_to_file(self) -> None:
        """Сохраняет все задачи в файл."""
        save_to_json_file(self._tasks, self._filepath)

    @property
    def task_data(self) -> Dict[str, Dict]:
        """Возвращает данные задачи по ее id."""
        return self._tasks.get(str(self.id), {})

    @task_data.setter
    def task_data(self, task_data: Dict[str, Dict]):
        """Перезаписывает данные задачи и сохраняет изменения в файл."""
        self._tasks[self.id] = task_data
        self._save_to_file()

    @classmethod
    def get_all_tasks(cls) -> dict:
        """Возвращает реестр всех задач."""
        return cls._tasks


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
