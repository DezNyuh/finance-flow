from models.expense import Expense
from services.storage import write_json, read_json
from ui.menu import menu

# print(expense1)
# print([expense1])

# expenses = [] 

# expense1 = Expense("Mc'Donalds", 29.90, "Snack", "Card", "24/07/2026") 
# expense2 = Expense('Burger King', 41.90, "Snack", "Pix", '24/07/2026') 
# expense3 = Expense('Market', 129.80, 'House', 'Card', '25/07/2026') 

# expenses.append(expense1) 
# expenses.append(expense2) 
# expenses.append(expense3) 

def add_expense():
    store_name = input('Name: ')
    amount = float(input('Amount: '))
    category = input('Category: ')
    payment_method = input('Payment method: ')
    release_date = input('Release date: ')
    return Expense(store_name, amount, category, payment_method, release_date)

def save_expense():
    expenses = read_json()
    new_expense = add_expense()
    expenses.append(new_expense)
    write_json(expenses)

def list_expenses():
    expenses = read_json()
    if not expenses:
        print(f'\nNo expenses found.')
        return None

    print('Expenses: ')
    for index, expense in enumerate(expenses, start = 1):
        print('=' * 40)
        print(f'{index}. {expense}')

    return 

    # expenses = read_json()
    # i = 0
    # if expenses:
    #     for expense in expenses:
    #         i += 1
    #         print(f'===' * 20)
    #         print()
    #         print(f'{i}.')
    #         print()
    #         print(expense)
    #         print()
    #     print('===' * 20)
    # else:
    #     print('No expenses found.')

def update_expense():

    expenses = read_json()

    if not expenses:
        print('No expenses found.')
        return
    
    index = 0
    
    expense = expenses[index]

    list_expenses()

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

    if option == '2':
        expense.amount = float(input('New amount: '))

    if option == '3':
        expense.category = input('New category: ')

    if option == '4':
        expense.payment_method = input('New payment method: ')

    if option == '5':
        expense.release_date = input('New release date: ')

    if option == '6':
        expense.store_name = input('New store name: ')
        expense.amount = float(input('New amount: '))
        expense.category = input('New category: ')
        expense.payment_method = input('New payment method: ')
        expense.release_date = input('New release date: ')

    else:
        print('Option not exists.')
        return

    expenses_dict = [
        expense.to_dict()
        for expense in expenses
    ]

    write_json(expenses_dict)

    print('Expense updated sucessfully!')



while True:
    choice = menu()

    if choice == '1':
        save_expense()

    elif choice == '2':
        list_expenses()

    elif choice == '3':
        update_expense()

    elif choice == '0':
        break