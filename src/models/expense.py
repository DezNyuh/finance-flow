class Expense:
    def __init__(self, store_name, amount, category, payment_method, release_date):
        self.store_name = store_name
        self.amount = amount
        self.category = category
        self.payment_method =  payment_method
        self.release_date = release_date  

    def __str__(self):
        return f"""Store: {self.store_name}\nAmount: {self.amount}\nCategory: {self.category}
Payment Method: {self.payment_method}
Realease Date: {self.release_date}"""

    def __repr__(self):
        return f"""Store: {self.store_name}\nAmount: {self.amount}\nCategory: {self.category}
Payment Method: {self.payment_method}
Realease Date: {self.release_date}"""
    


# expense = Expense("Mc'Donalds", 29.90, "Snack", "Card", "24/07/2026")
# print(expense)