from models.expense import Expense
from services.storage import write_json, read_json

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
    if expenses:
        for expense in expenses:
            print('---' * 20)
            print()
            print(expense)
            print()
        print('---' * 20)
    else:
        print('No expenses found.')

list_expenses()
