import pytest
from plates import is_valid

#Note: valid plates pass all requirements
def test_valid_plates():
 assert is_valid('CS50') == True
 assert is_valid('HELLO') == True
 assert is_valid('AA22') == True

#Note: minimum 2 characters required
def test_minimum_length():
 assert is_valid('H') == False
 assert is_valid('') == False

#Note: maximum 6 characters allowed
def test_maximum_length():
 assert is_valid('TOOLONG') == False
 assert is_valid('ABCDEFG') == False

#Note: must start with at least 2 letters
def test_start_with_letters():
 assert is_valid('2ABC') == False
 assert is_valid('A2BC') == False

#Note: numbers must come at end, no 0 first
def test_numbers_at_end():
 assert is_valid('AAA222') == True
 assert is_valid('AAA22A') == False
 assert is_valid('CS05') == False

#Note: no punctuation allowed
def test_no_punctuation():
 assert is_valid('PI3.14') == False
 assert is_valid('CS-50') == False
 assert is_valid('HELLO!') == False
