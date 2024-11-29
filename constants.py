import textwrap
from colorama import Fore, Style

HANDLERS = {
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
2 - Посмотреть список категорий
3 - Найти задачу (по ключевым словам, категории или статусу выполнения)
4 - Добавить задачу
5 - Изменить задачу
6 - Удалить задачу
0 - Выйти
{Style.RESET_ALL}
"""
WAIT_COMMAND = f"{Fore.BLUE}Ожидание ввода:{Style.RESET_ALL} "
CATEGORIES_FILEPATH = "data/categories.json"
TASKS_FILEPATH = "data/tasks.json"
