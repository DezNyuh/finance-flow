import json
from pathlib import Path 
from models.expense import Expense

EXPENSES_FILE = Path(__file__).parent.parent.parent / 'data' / 'expenses.json'

def write_json(expenses):
    list_expenses = []
    for expense in expenses:
        list_expenses.append(expense.__dict__)
    with open (EXPENSES_FILE, 'w', encoding='utf8') as f: 
        json.dump(list_expenses, f, indent=2) 

def read_json():
    try:
        with open(EXPENSES_FILE, 'r', encoding='utf8') as f:
            file_data = json.load(f)
        expenses = [
            Expense(**item)
            for item in file_data
        ]
    except (FileNotFoundError, json.JSONDecodeError):
        write_json([])
        return[]

    return expenses



    # with open('archive.json', 'r',) as f: # json.load(archive.json)