from expense import Expense
from storable import saveJSON

# print(expense1)
# print([expense1])

expenses = [] 

expense1 = Expense("Mc'Donalds", 29.90, "Snack", "Card", "24/07/2026") 
expense2 = Expense('Burger King', 41.90, "Snack", "Pix", '24/07/2026') 
expense3 = Expense('Market', 129.80, 'House', 'Card', '25/07/2026') 

expenses.append(expense1) 
expenses.append(expense2) 
expenses.append(expense3) 

saveJSON(expenses)

