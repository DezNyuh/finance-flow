import json
from pathlib import Path 

EXPENSES_FILE = Path(__file__).parent.parent / 'data' / 'expenses.json'

def saveJSON(expenses):

    list_expenses = []

    for expense in expenses:
        list_expenses.append(expense.__dict__)

    with open (EXPENSES_FILE, 'w', encoding='utf8') as f: 
        json.dump(list_expenses, f, indent=2) 




    # with open('archive.json', 'r',) as f: # json.load(archive.json)