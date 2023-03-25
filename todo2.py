#! /opt/miniconda3/bin/python3
'''
todo2 is an app that maintains a todo list
just as with the todo code in this folder.
but it also uses an Object Relational Mapping (ORM)
to abstract out the database operations from the
UI/UX code.
The ORM, TodoList, will map SQL rows with the schema
    (rowid,title,desc,completed)
to Python Dictionaries as follows:
(5,'commute','drive to work',false) <-->
{rowid:5,
 title:'commute',
 desc:'drive to work',
 completed:false)
 }
In place of SQL queries, we will have method calls.
This app will store the data in a SQLite database ~/todo.db
Recall that sys.argv is a list of strings capturing the
command line invocation of this program
sys.argv[0] is the name of the script invoked from the shell
sys.argv[1:] is the rest of the arguments (after arg expansion!)
Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists
'''

from todolist import TodoList
import sys


# here are some helper functions ...

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''menu:
            0. quit 
            1. show transactions (enter show)
            2. add transaction (enter add)
            3. delete transaction (enter delete)
            4. summarize transactions by date (enter date)
            5. summarize transactions by month (enter month)
            6. summarize transactions by year (enter year)
            7. summarize transactions by category (enter category)
            8. print this menu (enter print)
            '''
            )

def print_todos(todos):
    ''' print the todo items '''
    if len(todos)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-10s %-10s %-15s %-15s %-20s"%('item #','amount','cateory','date', 'description'))
    print('-'*70)
    for item in todos:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-10s %-10s %-15s %-15s %-20s"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to TodoList'''
    todolist = TodoList()
    print(arglist)
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_todos(todos = todolist.show())    
    elif arglist[0]=='add':
        if len(arglist)!=5:
            print_usage()
        else:
            todo = {'amount':arglist[1],'category':arglist[2],'date':arglist[3],'description':arglist[4]}
            todolist.add(todo)
        pass
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            todolist.delete(arglist[1])
    elif arglist[0]=="date":
        print_todos(todos = todolist.dateOrder())    
    elif arglist[0]=="month":
        print_todos(todos = todolist.monthOrder())
    elif arglist[0]=="year":
        print_todos(todos = todolist.yearOrder())      
    elif arglist[0]=="category":
        print_todos(todos = todolist.categoryOrder())    


    else:
        print(arglist,"is not implemented")
        print_usage()


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the name as a string
                args = ['add',args[1],args[2],args[3],args[4]]
            process_args(args)
            print('-'*70+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*70+'\n'*3)



toplevel()