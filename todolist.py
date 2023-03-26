'''
todolist.py is an Object Relational Mapping to the todolist database
The ORM will work map SQL rows with the schema
    (rowid,title,desc,completed)
to Python Dictionaries as follows:
(5,'commute','drive to work',false) <-->
{rowid:5,title:'commute',desc:'drive to work',completed:false)
In place of SQL queries, we will have method calls.
This app will store the data in a SQLite database ~/todo.db
'''
import sqlite3
import os

def toDict(t):
    ''' t is a tuple (rowid, amount, category, date, description)'''
    print('t='+str(t))
    todo = {'rowid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return todo

class TodoList():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS todo
                    (amount int, category text, date text, description text)''',())

    def show(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* FROM todo",())
    
    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        return self.runQuery("INSERT INTO todo VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        ''' delete a todo item '''
        return self.runQuery("DELETE FROM todo WHERE rowid=(?)",(rowid,))
    
    def dateOrder(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* FROM todo ORDER BY date",())

    def monthOrder(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* FROM todo ORDER BY SUBSTRING(date, 6, 7)",())    
    
    def yearOrder(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* FROM todo ORDER BY SUBSTRING(date, 1, 4)",())
    
    def categoryOrder(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* FROM todo ORDER BY category",())

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/otodo.db')
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]