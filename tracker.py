'''this is the method which give user a menu and user can modify
things through this method'''
import sys
from transaction import Transaction
def print_usage():
    ''' print an explanation of how to use this command '''
    print('''menu:
            0. quit 
            1. show transactions (enter show)
            2. add transaction (enter add, date fomat: YYYY-MM-DD)
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
        print('There is no transaction exist.')
        return
    print('\n')
    print("%-10s %-10s %-15s %-15s %-20s"%('item #','amount','cateory','date', 'description'))
    print('-'*70)
    for item in todos:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-10s %-10s %-15s %-15s %-20s"%values)
def process_args(arglist):
    '''this is a method which will process user's input and give respond'''
    transaction = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_todos(todos = transaction.show())
    elif arglist[0]=='add':
        if len(arglist)!=5:
            print_usage()
        else:
            todo = {'amount':arglist[1],'category':arglist[2],
                    'date':arglist[3],'description':arglist[4]}
            transaction.add(todo)
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_usage()
        else:
            transaction.delete(arglist[1])
    elif arglist[0]=="date":
        print_todos(todos = transaction.date_order())
    elif arglist[0]=="month":
        print_todos(todos = transaction.month_order())
    elif arglist[0]=="year":
        print_todos(todos = transaction.year_order())
    elif arglist[0]=="category":
        print_todos(todos = transaction.category_order())
    elif arglist[0] == "print":
        print_usage()
    elif arglist[0] == "quit":
        sys.exit(0)
    else:
        print(arglist,"is not implemented")
        print_usage()
def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                i = 5
                while i < len(args):
                    args[4] = args[4] + ' ' + args[i]
                    i = i + 1
                args = ['add',args[1],args[2],args[3],args[4]]
            process_args(args)
            print('-'*70+'\n'*3)
    else:
        args = sys.argv[1:]
        process_args(args)
        print('-'*70+'\n'*3)
toplevel()
