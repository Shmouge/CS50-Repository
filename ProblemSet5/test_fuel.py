import pytest
from fuel import convert, gauge

#Note: test convert function with valid fractions
def test_convert_valid():
 assert convert('3/4') == 75
 assert convert('1/4') == 25
 assert convert('4/4') == 100
 assert convert('0/4') == 0

#Note: test convert with zero division
def test_convert_zero_division():
 with pytest.raises(ZeroDivisionError):
 convert('4/0')

#Note: test convert with invalid values
def test_convert_value_error():
 with pytest.raises(ValueError):
 convert('three/four')
 with pytest.raises(ValueError):
 convert('1.5/3')

#Note: test convert with X > Y
def test_convert_x_greater_than_y():
 with pytest.raises(ValueError):
 convert('5/4')

#Note: test gauge function outputs
def test_gauge():
 assert gauge(1) == 'E'
 assert gauge(0) == 'E'
 assert gauge(99) == 'F'
 assert gauge(100) == 'F'
 assert gauge(25) == '25%'
 assert gauge(50) == '50%'
