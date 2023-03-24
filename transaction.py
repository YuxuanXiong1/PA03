import sqlite3
import os

def toDict(t):
    ''' t is a tuple (rowid, amount, category, date, description)'''
    print('t='+str(t))
    tran = {'rowid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description' :t[4]}
    return tran

class Transaction():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS
                    (amount int, category text, date text, descripition text)''',())
    
    def show_tran(self):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        return self.runQuery("SELECT * from tracker",())

    def selectAll(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo",())

    def selectCompleted(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo where completed=1",())

    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        return self.runQuery("INSERT INTO tracker VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        ''' delete a todo item '''
        return self.runQuery("DELETE FROM todo WHERE rowid=(?)",(rowid,))

    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE todo SET completed=1 WHERE rowid=(?)",(rowid,))

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/transactions.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]