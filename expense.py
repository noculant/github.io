class Expense:
    '''
    Creates a class to represent an individual expense.
    '''

    def __init__(self, date, payee, amount, category):
        self.date = date
        self.payee = payee
        self.amount = amount
        self.category = category
    '''
    Format the output when printing the class
    '''

    def __str__(self):
        return f"{self.date}: {self.payee} - {self.amount} ({self.category})"
