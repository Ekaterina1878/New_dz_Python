import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive()
@pytest.mark.parametrize("input_str, expected", [
    ("text", "Text"),
    ("hello world", "Hello world"),
    ("abc123", "Abc123"),
    ("тест", "Тест"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative()
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("123asd", "123asd"),
    ("   ", "   "),
    ("@$$%@", "@$$%@"),
])
def test_capitalise_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive()
@pytest.mark.parametrize("input_str, expected", [
    ("   test", "test"),
    ("  Hello world", "Hello world"),
    ("  ТЕСТ", "ТЕСТ"),
    ("  asd123", "asd123"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative()
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("test", "test"),
    ("   ", ""),
    ("дом 15 корпус 3  ", "дом 15 корпус 3  "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive()
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Text", "T", True),
    ("123ASD", "2", True),
    ("hello world", "o", True),
    ("тест", "е", True),
    ("HELLO!", "!", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative()
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Text", "K", False),
    ("hello world", "p", False),
    ("тест", "у", False),
    (None, "a", False),
    ("test", "", False),
    ("888", "7", False),
    ("HELLO!", "$", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive()
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Text", "x", "Tet"),
    ("hello world", "o", "hell wrld"),
    ("АВТОБУС", "БУС", "АВТО"),
    ("123", "12", "3"),
    ("Pochta@moya", "@", "Pochtamoya"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative()
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Text", "K", "Text"),
    ("hello world", "v", "hello world"),
    ("автобус", "кит", "автобус"),
    ("", "a", ""),
    ("Pochta@moya", "$", "Pochta@moya"),
    ("test", "", "test"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
