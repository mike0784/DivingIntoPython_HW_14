
import os
import pack.ListDir as ld
import pack.WriteJsonFile as jf



def work(file: str) -> None:
    """Главная функция. Управляет функциями listDirectories() и writeToJSON
    >>> work(result.json)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'list' object has no attribute 'json'
    >>> work("result.json")
    """
    result = list()
    file = os.getcwd() + "/" + file
    result = ld.listDirectories("i:/DOS")
    print(file)
    jf.writeToJSON(result, file)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
