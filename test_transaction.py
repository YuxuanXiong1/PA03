from transaction import Transaction
import pytest

def test_add():
    ''' constructor should create a printable object '''
    tran = Transaction()
    todo = {'amount':10,'category':'apple',
                    'date':'2021/09/26','description':'this is apple'}
    tran.add(todo)
    t_quat = tran
    assert t_quat== <transaction.Transaction object at 0x7f2b3b386ce0>


def test_mul():
    q1 = Transaction(0,1,2,3)
    q2 = Transaction(0,-1,-2,-3)
    expected =Transaction(14,0,0,0)
    assert q1.conjugate()==q2
    assert q1*q2==expected

def test_to_dict():
    q1 = Transaction(2,7,1,8)
    expected = {'w':2,'x':7,'y':1,'z':8}
    assert q1.to_dict()==expected

def test_div_by_zero():
    q1 = Transaction(1,0,0,0)
    q0 = Transaction(0,0,0,0)
    with pytest.raises(Exception):
        q = q1/q0

def test_normalize_zero():
    q0 = Transaction(0,0,0,0)
    with pytest.raises(Exception):
        q = q0.normalize()
