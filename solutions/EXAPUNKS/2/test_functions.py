from functions import *
from registers import get_register, set_register

def test_COPY():
    COPY('10', 'X')
    assert get_register('X') == 10


def test_ADDI():
    set_register('X', 10)
    ADDI('10', 'X', 'X')
    assert get_register('X') == 20


def test_SUBI():
    set_register('X', 10)
    SUBI('X', '10', 'X')
    assert get_register('X') == 0


def test_MULI():
    set_register('X', 10)
    MULI('X', '10', 'X')
    assert get_register('X') == 100


def test_DIVI():
    set_register('X', 17)
    DIVI('X', '5', 'X')
    assert get_register('X') == 3


def test_MODI():
    set_register('X', 17)
    MODI('X', '5', 'X')
    assert get_register('X') == 2
