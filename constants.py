import textwrap

HANDLERS = {
    "task_list": "view_task_list",
    "task": "view_task_by_name",
    "category_list": "view_category_list",
    "category": "view_tasks_by_category",
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
MAIN_MENU = """
Введите число, чтобы выполнить соответствующее действие:\n
1 - Посмотреть список задач
2 - Посмотреть список категорий
3 - Найти задачу (по ключевым словам, категории или статусу выполнения)
4 - Добавить задачу
5 - Изменить задачу
6 - Удалить задачу
"""
CATEGORIES_FILEPATH = "data/categories.json"
