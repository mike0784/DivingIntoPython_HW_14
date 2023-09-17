import json

def writeToJSON(ls: list, file: str) -> None:
    """Функция сохранеет результат работы функции listDirectories в json файл"""
    with open(file, "w") as f:
        json.dump(ls, f)