import json


def open_json_file(filepath: str) -> dict:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return {}


def save_to_json_file(content: dict, filepath: str) -> None:
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(content, file, ensure_ascii=False, indent=4)
