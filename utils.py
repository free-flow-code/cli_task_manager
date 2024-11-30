import json
from typing import Optional
from pydantic import ValidationError
from models import TaskCreateModel, TaskUpdateModel
from prettytable import PrettyTable
from constants import CLI_MESSAGES


def print_tasks(data: dict[str, dict]) -> None:
    table = PrettyTable()
    table.field_names = ["ID"] + list(next(iter(data.values())).keys())

    for key, value in data.items():
        table.add_row([key, *value.values()])
    print(table)


def validate_data(data: str | dict, creating: bool = True) -> Optional[dict]:
    try:
        if not data:
            print(CLI_MESSAGES.get("empty_data"))
            return

        if isinstance(data, str):
            quote = "'"
            double_quote = '"'
            data = data.replace(quote, double_quote)
            data = json.loads(data)

        if creating:
            validated_data = TaskCreateModel(**data)
        else:
            validated_data = TaskUpdateModel(**data)

        return validated_data.dict()
    except json.JSONDecodeError:
        print(CLI_MESSAGES.get("incorrect_data"))
        return
    except ValidationError as err:
        print("Ошибки валидации:")
        for error in err.errors():
            print(f"- {error['loc'][0]}: {error['msg']}")
        return
