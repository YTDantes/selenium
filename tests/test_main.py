from src.main import A
import pytest

# фикстуры (Предусловия, поступсловия)
@pytest.fixture()
def before_after():
    print("Before test")
    yield
    print("\nAfter test")

def test_main():
    assert A.x == 1

def test_2(before_after):
    assert 2 == 2

# запуск pytest -v
# добавить файл pytest.ini

