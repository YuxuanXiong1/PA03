'''this is the basic program which store the information of transaction'''
import sqlite3
import os
def to_dict(tupl):
    ''' t is a tuple (rowid, amount, category, date, description)'''
    print('t='+str(tupl))
    todo = {'rowid':tupl[0], 'amount':tupl[1], 'category':tupl[2],
            'date':tupl[3], 'description':tupl[4]}
    return todo
class Transaction():
    '''this is a class withc initial the transaction and give method to modify it.'''
    def __init__(self):
        self.run_query('''CREATE TABLE IF NOT EXISTS todo
                    (amount int, category text, date text, description text)''',())
    def show(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.run_query("SELECT rowid,* FROM todo",())
    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        return self.run_query("INSERT INTO todo VALUES(?,?,?,?)",
                             (item['amount'],item['category'],item['date'],item['description']))
    def delete(self,rowid):
        ''' delete a todo item '''
        return self.run_query("DELETE FROM todo WHERE rowid=(?)",(rowid,))
    def date_order(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.run_query("SELECT rowid,* FROM todo ORDER BY SUBSTRING(date,9,10)",())
    def month_order(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.run_query("SELECT rowid,* FROM todo ORDER BY SUBSTRING(date,6,7)",())
    def year_order(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.run_query("SELECT rowid,* FROM todo ORDER BY SUBSTRING(date, 1, 4)",())
    def category_order(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.run_query("SELECT rowid,* FROM todo ORDER BY category",())
    def run_query(self,query,tuple1):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/otodo.db')
        cur = con.cursor()
        cur.execute(query,tuple1)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
    