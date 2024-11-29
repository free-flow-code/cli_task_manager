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
    "task_not_found": f"{Fore.YELLOW}Задача не найдена. Проверьте правильность ввода.{Style.RESET_ALL}",
    "incorrect_task_name": f"{Fore.YELLOW}Введите название задачи. Или '--name all', чтобы посмотреть все задачи.{Style.RESET_ALL}",
}
