import pytest
from src.keyboard import KeyBoard


def test_keyboard_change_lang():
    kb = KeyBoard("123", 100, 500)

    assert kb.language == "EN"

    kb.change_lang()
    assert kb.language == "RU"

    kb.change_lang()
    assert kb.language == "EN"

    kb.change_lang()
    assert kb.language == "RU"


def test_keyboard_str():
    kb = KeyBoard("123", 100, 500)

    assert str(kb) == "123"
