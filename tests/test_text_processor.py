"""
Lab 6 - TextProcessor tests (student version)

Every test below starts with the annotation  @pytest.mark.skip(reason=TODO).
For each test:
    1. Remove the @pytest.mark.skip line.
    2. Replace `pass` with real test code.
    3. Run pytest and read the coverage report.

Each test here is one function that runs many times, once per row of its
@pytest.mark.parametrize table. Add a row = add a test case.

If one row fails because of a real bug in src/, document only that row:

    pytest.param("hello", "olleh",
                 marks=pytest.mark.xfail(reason="BUG #N: ...", strict=True)),
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.text_processor import TextProcessor

TODO = "TODO: remove this annotation once you write the test"

# Marks every test in this file. Run only these with:  pytest -m text
pytestmark = pytest.mark.text

BUG_REVERSE = pytest.mark.xfail(
    reason="BUG #5: reverse() returns the text unchanged instead of reversed", strict=True)
BUG_VOWELS = pytest.mark.xfail(
    reason="BUG #6: count_vowels() is case-sensitive (ignores uppercase vowels)", strict=True)
BUG_PALINDROME = pytest.mark.xfail(
    reason="BUG #7: is_palindrome() does not ignore spaces and case", strict=True)
BUG_WORD_COUNT = pytest.mark.xfail(
    reason="BUG #8: word_count() uses split(' ') so extra/leading/trailing spaces count as words",
    strict=True)
BUG_TRUNCATE = pytest.mark.xfail(
    reason="BUG #9: truncate() appends '...' even when the text is not truncated", strict=True)


# ---------------------------------------------------------------- fixtures

@pytest.fixture
def tp():
    """A TextProcessor for each test."""
    return TextProcessor()


# ----------------------------------------------------------------- reverse

@pytest.mark.parametrize("text, expected", [
    ("a", "a"),
    ("", ""),
    pytest.param("hello", "olleh", marks=BUG_REVERSE),
    pytest.param("ab", "ba", marks=BUG_REVERSE),
])
def test_reverse(tp, text, expected):
    """reverse(text) should equal expected."""
    assert tp.reverse(text) == expected


# ------------------------------------------------------------ count_vowels

@pytest.mark.parametrize("text, expected", [
    ("hello", 2),
    ("xyz", 0),
    ("", 0),
    pytest.param("HELLO", 2, marks=BUG_VOWELS),
    pytest.param("AEIOU", 5, marks=BUG_VOWELS),
])
def test_count_vowels(tp, text, expected):
    """count_vowels(text) should equal expected. It must ignore case."""
    assert tp.count_vowels(text) == expected


# ----------------------------------------------------------- is_palindrome

@pytest.mark.parametrize("text, expected", [
    ("racecar", True),
    ("hello", False),
    ("", True),
    pytest.param("nurses run", True, marks=BUG_PALINDROME),
    pytest.param("Racecar", True, marks=BUG_PALINDROME),
    pytest.param("Race car", True, marks=BUG_PALINDROME),
])
def test_is_palindrome(tp, text, expected):
    """is_palindrome(text) should be expected. It must ignore spaces and case."""
    assert tp.is_palindrome(text) is expected


# -------------------------------------------------------------- word_count

@pytest.mark.parametrize("text, expected", [
    ("the quick brown fox", 4),
    ("hello", 1),
    pytest.param("hello   world", 2, marks=BUG_WORD_COUNT),
    pytest.param("  hello   world  ", 2, marks=BUG_WORD_COUNT),
    pytest.param("", 0, marks=BUG_WORD_COUNT),
])
@pytest.mark.edge
def test_word_count(tp, text, expected):
    """word_count(text) should equal expected."""
    assert tp.word_count(text) == expected


# -------------------------------------------------------- capitalize_words

@pytest.mark.parametrize("text, expected", [
    ("hello world", "Hello World"),
    ("PYTHON", "Python"),
    ("", ""),
])
def test_capitalize_words(tp, text, expected):
    """capitalize_words(text) should equal expected. (This method has no bug.)"""
    assert tp.capitalize_words(text) == expected


# ---------------------------------------------------------------- truncate

@pytest.mark.parametrize("text, max_length, expected", [
    ("Hello World", 5, "Hello..."),
    ("abc", 0, "..."),
    pytest.param("Hi", 5, "Hi", marks=BUG_TRUNCATE),
    pytest.param("Hello", 5, "Hello", marks=BUG_TRUNCATE),
    pytest.param("", 3, "", marks=BUG_TRUNCATE),
])
@pytest.mark.edge
def test_truncate(tp, text, max_length, expected):
    """truncate(text, max_length) should equal expected."""
    assert tp.truncate(text, max_length) == expected
