import textwrap
from colorama import Fore, Style

ARGS_HANDLERS = {
    "view": "view_task",
    "add": "add_task",
    "edit": "edit_task",
    "find": "find_task",
    "delete": "delete_task",
}
LOGO = textwrap.dedent(
    """\
 ████████  █████   ██████ ██   ██ ██    ██
    ██    ██   ██ ██      ██  ██   ██  ██
    ██    ███████  ██████ █████      ██ 
    ██    ██   ██      ██ ██  ██     ██  
    ██    ██   ██ ██████  ██   ██    ██   
    """
)
MAIN_MENU = f"""{Fore.YELLOW}
Введите число, чтобы выполнить соответствующее действие:
1 - Посмотреть список задач
2 - Добавить задачу
3 - Изменить задачу
4 - Найти задачу (по названию, категории или статусу выполнения)
5 - Удалить задачу
0 - Выйти
{Style.RESET_ALL}
"""
MAIN_MENU_HANDLERS = {
    1: "show_view_task_menu",
    2: "show_add_task_menu",
    3: "show_edit_task_menu",
    4: "show_find_task_menu",
    5: "show_delete_task_menu",
    0: "exit"
}
INPUT_ERROR = f"{Fore.RED}Некорректный ввод.{Style.RESET_ALL}"
WAIT_COMMAND = f"{Fore.BLUE}Ожидание ввода:{Style.RESET_ALL} "
CATEGORIES_FILEPATH = "data/categories.json"
TASKS_FILEPATH = "data/tasks.json"
CLI_MESSAGES = {
    "incorrect_params": f"{Fore.RED}Не верно указаны параметры. Для справки: python main.py -h{Style.RESET_ALL}",
    "task_not_found": f"{Fore.YELLOW}Задача не найдена. Проверьте правильность ввода.{Style.RESET_ALL}",
    "incorrect_task_name": f"{Fore.YELLOW}Введите название задачи. Или '--name all', чтобы посмотреть все задачи.{Style.RESET_ALL}",
    "incorrect_data": f"{Fore.YELLOW}Неверный формат данных.{Style.RESET_ALL}",
    "empty_data": f"{Fore.YELLOW}Данные не переданы.{Style.RESET_ALL}",
    "success_add_task": f"{Fore.BLUE}Новая задача успешно добавлена.{Style.RESET_ALL}",
    "success_update_task": f"{Fore.BLUE}Задача успешно обновлена.{Style.RESET_ALL}",
    "task_already_exist": f"{Fore.RED}{{err}}{Style.RESET_ALL}",
    "category_not_found": f"{Fore.RED}Такой категории не существует.{Style.RESET_ALL}",
    "task_not_found_by_category": f"{Fore.YELLOW}В данной категории нет задач.{Style.RESET_ALL}",
    "task_not_found_by_keyword": f"{Fore.YELLOW}По данным ключевым словам задач не найдено.{Style.RESET_ALL}",
    "task_not_found_by_status": f"{Fore.YELLOW}Нет задач с таким статусом.{Style.RESET_ALL}",
    "incorrect_find_data": f"{Fore.YELLOW}Укажите категорию, ключевые слова или статус задачи для поиска.{Style.RESET_ALL}",
    "incorrect_status": f"{Fore.YELLOW}Некорректное значение статуса: {{status}}{Style.RESET_ALL}"
}
