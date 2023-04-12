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

    def get_total_expenses(self):
        return sum([record['amount'] for record in self.expense_records])
