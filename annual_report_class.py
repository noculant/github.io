class AnnualReport:
    """
    Represents the annual report which calculates totals for each category 
    of expenses, the total income from tenants, and the net profit for
    the landlord.
    """
    def __init__(self, rental_income_record, expense_record):
        """
        Constructs an instance of the rental income record
        and the expense record.

        expense_records: The list of expenses created
        """
        self.rental_income_record = rental_income_record
        self.expense_record = expense_record

    def get_total_rental_income(self):
        return self.rental_income_record.get_total_rental_income()

    def get_total_expenses(self):
        return self.expense_record.get_total_expenses()

    def get_net_income(self):
        return self.get_total_rental_income() - self.get_total_expenses()

    def generate_annual_report(self):
        total_rental_income = self.rental_income_record.get_total_income()
        total_expenses = self.expense_record.get_total_expenses()

        expense_categories = ['Mortgage', 'Repairs', 'Utilities', 'Taxes', 'Insurance']
        total_expenses_by_category = {}
        for category in expense_categories:
            total_expenses_by_category[category] = self.expense_record.get_total_expenses_by_category(category)

        profit = total_rental_income - total_expenses
        return {
            'total_rental_income': total_rental_income,
            'total_expenses': total_expenses,
            'total_expenses_by_category': total_expenses_by_category,
            'profit': profit
        }