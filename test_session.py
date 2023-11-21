import pytest

from session import add_numbers

def test_add_pos():
   assert add_numbers(1,2) == 3

def test_add_neg():
   assert add_numbers(1,-2) == -1

def test_add_zero():
   assert add_numbers(1,0) == 1

def test_add_neg_neg():
   assert add_numbers(-1,-2) == -3


