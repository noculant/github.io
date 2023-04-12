class ExpenseRecord:
    def __init__(self):
        self.expense_records = []

    def add_expense(self, date, payee, amount, category):
        expense = {
            "date": date,
            "payee": payee,
            "amount": amount,
            "category": category
        }
        self.expense_records.append(expense)

    def get_expenses_by_category(self, category):
        expenses = [record for record in self.expense_records if record['category'] == category]
        return expenses

    def get_total_expense_by_category(self, category):
        expenses = self.get_expenses_by_category(category)
        total_expense = sum([expense['amount'] for expense in expenses])
        return total_expense

    def get_all_expenses(self):
        return self.expense_records

    def get_total_expenses(self):
        return sum([record['amount'] for record in self.expense_records])
