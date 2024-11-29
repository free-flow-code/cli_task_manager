from prettytable import PrettyTable


def print_tasks(data: dict[str, dict]) -> None:
    table = PrettyTable()
    table.field_names = ["ID"] + list(next(iter(data.values())).keys())

    for key, value in data.items():
        table.add_row([key, *value.values()])
    print(table)
