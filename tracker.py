from transaction import Transaction
import sys


# here are some helper functions ...

def print_menu():
    ''' print an explanation of how to use this command '''
    print('''menu:
            0. quit 
            1. show transactions
            2. add transaction
            3. delete transaction
            4. summarize transactions by date
            5. summarize transactions by month
            6. summarize transactions by year
            7. summarize transactions by category
            8. print this menu
            '''
            )

def print_trans(trans):
    ''' print the transactions '''
    if len(trans)==0:
        print('no transaction to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-10s"%('item #','amount','category','date','description'))
    print('-'*40)
    for item in trans:
        values = tuple(item.values()) 
        print("%-10s %-10s %-10s %-10s %-10s"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to transaction'''
    transaction = Transaction()
    if arglist==[]:
        print_menu()
    elif arglist[0]=="show transactions":
        print_trans(trans = transaction.show_tran())
    elif arglist[0]=="showcomplete":
        print_trans(transaction.selectCompleted())
    elif arglist[0]=='add transaction':
        if len(arglist)!=3:
            print_menu()
        else:
            todo = {'title':arglist[1],'desc':arglist[2],'completed':0}
            transaction.add(todo)
    elif arglist[0]=='complete':
        if len(arglist)!= 2:
            print_menu()
        else:
            transaction.setComplete(arglist[1])
    elif arglist[0]=='delete':
        if len(arglist)!= 2:
            print_menu()
        else:
            transaction.delete(arglist[1])
    else:
        print(arglist,"is not implemented")
        print_menu()


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_menu()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the name as a string
                args = ['add',args[1]," ".join(args[2:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

    

toplevel()
