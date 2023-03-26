import pytest
import sqlite3
from transaction import Transaction, to_dict

@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [(2, "apple", "2021-03-12", "These are apples."), 
            (3, "orange", "2023-04-17", "These are oranges."),
            (7, "apple", "2022-01-09", "These are apples."),
            (1, "pineapple", "2020-03-21", "These are pineapples."),
           ]

@pytest.fixture
def returned_tuples(tuples):
    " add a rowid to the beginning of each tuple "
    return [(i+1,)+tuples[i] for i in range(len(tuples))]

@pytest.fixture
def returned_dicts(tuples):
    " add a rowid to the beginning of each tuple "
    return to_dict([(i+1,)+tuples[i] for i in range(len(tuples))])

@pytest.fixture
def todo_path(tmp_path):
    yield tmp_path / 'qotodo.db'

@pytest.fixture(autouse=True)
def todolist(todo_path,tuples):
    "create and initialize the todo.db database in /tmp "
    con= sqlite3.connect(todo_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS todo
                    (amount int, category text, date text, description text)''')
    for i in range(len(tuples)):
        cur.execute('''insert into todo values(?,?,?,?)''',tuples[i])
    # create the todolist database
    con.commit()
    td = Transaction()
    yield td
    cur.execute('''drop table todo''')
    con.commit()


def test_show(todolist,returned_dicts):
    td = todolist
    results = td.show()
    expected = returned_dicts
    assert results == expected

def test_add(todolist,returned_dicts):
    td = todolist
    tuple = (len(returned_dicts) + 1, 5, "pear", "2021-07-09", "These are pears.")
    todolist.add(to_dict(tuple))
    results = td.show()
    assert results[-1] == to_dict(tuple)

def test_delete(todolist,returned_dicts):
    td = todolist
    td.delete(1)
    results = td.show()
    expected = returned_dicts
    assert results == expected[1:]
