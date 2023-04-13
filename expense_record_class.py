class ExpenseRecord:
    """
    Represents the list of expenses from the landlord.
    """
    def __init__(self):
        """
        Constructs a list for the expense record to hold the 
        information for each expense.

        expense_records: The list of expenses
        """
        self.expense_records = []

    def add_expense(self, date, payee, amount, category):
        """
        Appends a dictionary of data for each expense payment to
        the list.

        date: The date of the payment
        payee: Company or person paid by landlord
        amount: The amount payed by the tenant
        category: The type of expense (mortgage, repairs, utilities, etc.)
        """
        expense = {
            "date": date,
            "payee": payee,
            "amount": amount,
            "category": category
        }
        self.expense_records.append(expense)

    def get_total_expenses(self):
        """
        Calculates the sum of the total expenses in the expense record.
        """
        return sum([record['amount'] for record in self.expense_records])

    def get_total_expenses_by_category(self, category):
        """
        Calculates the sum of the total expenses for a single category
        passed as a parameter.

        category: The category to calculate the sum for
        """
        return sum(expense['amount'] for expense in self.expense_records if expense['category'] == category)