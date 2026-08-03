from models.expense import Expense
from services.storage import write_json, read_json


def add_expense():
    store_name = input('Name: ')
    amount = float(input('Amount: '))
    category = input('Category: ')
    payment_method = input('Payment method: ')
    release_date = input('Release date: ')
    return Expense(store_name, amount, category, payment_method, release_date)

def save_expense():
    write_json(read_json() + [add_expense()])

def list_expenses():
    expenses = read_json()
    if not expenses:
        print('\nNo expenses found.')
        return

    print('Expenses: ')
    for index, expense in enumerate(expenses, start = 1):
        print('=' * 40)
        print(f'{index}. {expense}')
    return 

def update_expense():
    expenses = read_json()
    if not expenses:
        print('\nNo expenses found.')
        return
    list_expenses()

    while True:
        index = int(input('\nWhich expense do you want to edit? '))
        try:
            expense = expenses[index - 1]
            break
        except IndexError:
            print('\nYou type out of range.')

    print('\nWhat do you want to edit?')
    print('1 - Store name')
    print('2 - Amount')
    print('3 - Category')
    print('4 - Payment method')
    print('5 - Release Date')
    print('6 - Everything')

    option = input('Choice an option: ')
    if option == '1':
        expense.store_name = input('New store name: ')

    elif option == '2':
        expense.amount = float(input('New amount: '))

    elif option == '3':
        expense.category = input('New category: ')

    elif option == '4':
        expense.payment_method = input('New payment method: ')

    elif option == '5':
        expense.release_date = input('New release date: ')
        
    elif option == '6':
        expense.store_name = input('New store name: ')
        expense.amount = float(input('New amount: '))
        expense.category = input('New category: ')
        expense.payment_method = input('New payment method: ')
        expense.release_date = input('New release date: ')
    else:
        print('Option not exists.')
        return

    write_json(expenses)
    print('Expense updated sucessfully!')

def delete_expense():
    expenses = read_json()
    if not expenses:
        print('\nNo expenses found.')
        return
    
    list_expenses()


    while True:
        index = int(input('\nWhich expense do you want to delete? '))

        try:
            expenses.pop(index - 1)
            write_json(expenses)
            print('Expense deleted sucessfully!')
            break

        except IndexError:
            print('\nYou type out of range.')
            continue