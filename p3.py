import pytest
from p1 import work

def test_one_work():
    assert work("result.json") == None, "Тест провылен"

def test_two_work():
    assert work("rr") == None, "Тест провылен"


if __name__ == "__main__":
    pytest.main()