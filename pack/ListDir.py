import os
__all__ = ["listDirectories"]
def listDirectories(dir: str) -> list:
    """Данная функция создает список каталогов и файлов
    """
    result = list()
    os.chdir(dir)
    content = os.listdir()
    for obj in content:
        if os.path.isfile(obj):
            size = os.path.getsize(obj)
            temp = {"file": obj, "parent": dir, "type": "file", "size": size}
            result.append(temp)
        if os.path.isdir(obj):
            size = os.path.getsize(obj)
            temp = {"file": obj, "parent": dir, "type": "directories", "size": size}
            result.append(temp)
            listDirectories(obj)
    os.chdir("..")
    return result