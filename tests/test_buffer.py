import pytest
from meli_lib.meli import Buffer

def test_fifo_policy():
    buffer = Buffer('FIFO')
    buffer.insert(1)
    buffer.insert(2)
    buffer.insert(3)
    assert buffer.extract() == 1
    assert buffer.extract() == 2
    assert buffer.extract() == 3

def test_lifo_policy():
    buffer = Buffer('LIFO')
    buffer.insert(1)
    buffer.insert(2)
    buffer.insert(3)
    assert buffer.extract() == 3
    assert buffer.extract() == 2
    assert buffer.extract() == 1

def test_invalid_policy():
    with pytest.raises(ValueError):
        Buffer('INVALID')