import pytest
from bank import value

#Note: exact hello cases return $0
def test_hello_exact():
 assert value('hello') == 0
 assert value('Hello') == 0
 assert value('HELLO') == 0

#Note: hello with additional text still $0
def test_hello_with_more():
 assert value('hello, Newman') == 0
 assert value('Hello there') == 0

#Note: words starting with h (not hello) return $20
def test_h_words():
 assert value('hey') == 20
 assert value('hi') == 20
 assert value('How you doing?') == 20

#Note: words not starting with h return $100
def test_other_words():
 assert value('What''s happening?') == 100
 assert value('Good morning') == 100
 assert value('sup') == 100
