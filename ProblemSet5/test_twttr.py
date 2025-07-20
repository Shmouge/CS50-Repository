import pytest
from twttr import shorten

#Note: lowercase vowels removed
def test_lowercase_vowels():
    assert shorten("aeiou") == ""
    assert shorten("hello") == "hll"

#Note: uppercase vowels removed
def test_uppercase_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("WORLD") == "WRLD"

#Note: mixed case and non-letters remain
def test_mixed_and_punctuation():
    assert shorten("Cs50! Is Awesome?") == "Cs50! s wsm?"
    assert shorten("123AEi!") == "123!"

#Note: words without vowels unchanged
def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
    assert shorten("") == ""

#Note: preserve consonants and order
def test_preserve_order():
    input_str = "Python Programming"
    expected = "Pythn Prgrmmng"
    assert shorten(input_str) == expected