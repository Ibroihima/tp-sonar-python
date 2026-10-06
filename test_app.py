import pytest
from app import add, divide, is_even, read_config, classify


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_is_even():
    assert is_even(4)
    assert not is_even(7)
"""
def test_read_config(tmp_path):
    p = tmp_path / "conf.txt"
    p.write_text("hello", encoding="utf-8")
    assert read_config(str(p)) == "hello"
def test_classify():
    assert classify(20) == "grand"
    assert classify(1) == "petit"
"""