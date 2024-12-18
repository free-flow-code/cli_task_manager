from enum import Enum
from datetime import date
from pydantic import BaseModel, Field, field_validator
from typing import Dict, List, Optional
from constants import (
    CATEGORIES_FILEPATH,
    TASKS_FILEPATH,
    CLI_MESSAGES
)
from files_processing import open_json_file, save_to_json_file


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

    @classmethod
    def get_task_ids_by_category(cls, category_name: str) -> Optional[List[int]]:
        """Возвращает список id задач для заданной категории."""
        category_task_ids = cls._categories.get(category_name, None)
        if category_task_ids is None:
            print(CLI_MESSAGES.get("category_not_found"))
            return
        return category_task_ids


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
        title = kwargs.get("title", "Без названия")
        if self._title_exists(title):
            raise ValueError(f"Задача с названием '{title}' уже существует.")

        self.id: str = kwargs.get("id", str(self._tasks_count + 1))
        self.title: str = title
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

    @classmethod
    def _save_to_file(cls) -> None:
        """Сохраняет все задачи в файл."""
        save_to_json_file(cls._tasks, cls._filepath)

    @property
    def task_data(self) -> Dict[str, Dict]:
        """Возвращает данные задачи"""
        return self._tasks.get(str(self.id), {})

    @task_data.setter
    def task_data(self, task_data: Dict[str, Dict]) -> None:
        """Перезаписывает данные задачи и сохраняет изменения в файл."""
        self._tasks[self.id] = task_data
        self._save_to_file()

    @classmethod
    def get_task_by_id(cls, task_id) -> Optional[dict]:
        """Возвращает данные задачи по ее id."""
        if task_id in cls._tasks:
            return {task_id: cls._tasks.get(task_id)}
        return

    @classmethod
    def get_task_by_name(cls, task_name):
        """Возвращает данные задачи по ее названию."""
        for task_id, task_data in cls._tasks.items():
            if task_data["title"] == task_name:
                return cls.get_task_by_id(task_id)
        return

    @classmethod
    def update_task_by_id(cls, task_id: str, data: dict) -> Optional[dict]:
        """Обновляет данные задачи по её id."""
        if task_id in cls._tasks:
            task_data = cls._tasks.get(task_id)
            del data["title"]
            task_data.update(data)
            updated_data = {task_id: task_data}
            cls._tasks.update(updated_data)
            cls._save_to_file()
            return updated_data
        return

    @classmethod
    def update_task_by_name(cls, task_name: str, data: dict) -> Optional[dict]:
        """Обновляет данные задачи по её названию (title)."""
        for task_id, task_data in cls._tasks.items():
            if task_data["title"] == task_name:
                return cls.update_task_by_id(task_id, data)
        return

    @classmethod
    def find_tasks_by_category(cls, category: str) -> Optional[dict]:
        """Поиск задач в указанной категории. Возвращает словарь с данными задач."""
        category_task_ids = Category.get_task_ids_by_category(category)
        if category_task_ids is None:
            return
        elif not category_task_ids:
            print(CLI_MESSAGES.get("task_not_found_by_category"))
            return

        matched_tasks = {}
        for task_id in category_task_ids:
            matched_tasks.update({task_id: cls._tasks.get(str(task_id))})
        return matched_tasks

    @classmethod
    def find_tasks_by_keyword(cls, keyword: str) -> Optional[dict]:
        """Поиск задач по ключевым словам. Возвращает словарь с данными задач."""
        matched_tasks = {}
        for task_id, task_data in cls.get_all_tasks().items():
            if keyword.lower() in task_data["title"].lower():
                matched_tasks.update({task_id: task_data})
        if not matched_tasks:
            print(CLI_MESSAGES.get("task_not_found_by_keyword"))
            return
        return matched_tasks

    @classmethod
    def find_tasks_by_status(cls, status: str) -> Optional[dict]:
        """Поиск задач по их статусу. Возвращает словарь с данными задач."""
        status = status.capitalize()
        if status in TaskStatus._value2member_map_:
            matched_tasks = {}
            for task_id, task_data in cls.get_all_tasks().items():
                if status == task_data["status"]:
                    matched_tasks.update({task_id: task_data})

            if not matched_tasks:
                print(CLI_MESSAGES.get("task_not_found_by_status"))
                return
            return matched_tasks
        else:
            print(CLI_MESSAGES.get("incorrect_status").format(status=status))

    @classmethod
    def _title_exists(cls, title: str) -> bool:
        """Проверяет, существует ли задача с заданным названием."""
        return any(task["title"] == title for task in cls._tasks.values())

    @classmethod
    def get_all_tasks(cls) -> dict:
        """Возвращает реестр всех задач."""
        return cls._tasks

    @classmethod
    def delete_task_by_id(cls, task_id: str) -> bool:
        """Удаляет задачу по её id и сохраняет изменения в файл."""
        if task_id not in cls._tasks:
            return False

        del cls._tasks[task_id]
        cls._save_to_file()
        return True

    @classmethod
    def delete_task_by_name(cls, task_name: str) -> bool:
        """Удаляет задачу по её названию и сохраняет изменения в файл."""
        for task_id, task_data in cls._tasks.items():
            if task_data["title"] == task_name:
                return cls.delete_task_by_id(task_id)
        return False


class TaskCreateModel(BaseModel):
    title: str
    description: Optional[str] = Field(default="")
    category: Optional[str] = Field(default="Общее")
    due_date: Optional[date] = Field(default_factory=date.today)
    priority: TaskPriority = Field(default=TaskPriority.middle)
    status: TaskStatus = Field(default=TaskStatus.not_done)

    @field_validator('priority', mode='before')
    def validate_priority(cls, value):
        if isinstance(value, str):
            value = value.capitalize()
        return value

    @field_validator('status', mode='before')
    def validate_status(cls, value):
        if isinstance(value, str):
            value = value.capitalize()
        return value

    def dict(self, *args, **kwargs):
        result = super().dict(*args, **kwargs)
        result['due_date'] = str(result['due_date'])
        result['priority'] = result['priority'].value  # Получаем строковое значение из перечисления
        result['status'] = result['status'].value  # Получаем строковое значение из перечисления
        return result


class TaskUpdateModel(TaskCreateModel):
    title: Optional[str] = None

    class Config:
        extra = "forbid"  # Запрещает добавлять неизвестные поля для обновлений
