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

        expense_records: The list of expenses created from expense class
        rental_income_record: The list of tenant payments made to landlord
        """
        self.rental_income_record = rental_income_record
        self.expense_record = expense_record

    def get_total_rental_income(self):
        """
        Call the get_total_rental_income function from the rental income
        class and return the result.
        """
        return self.rental_income_record.get_total_rental_income()

    def get_total_expenses(self):
        """
        Call the get_total_expenses function from the rental income
        class and return the result.
        """
        return self.expense_record.get_total_expenses()

    def get_net_income(self):
        """
        Calculate the net profit using the previous calculations.
        """
        return self.get_total_rental_income() - self.get_total_expenses()

    def generate_annual_report(self):
        """
        Calculate the net profit using the previous calculations.  Calculate the 
        total spent on each category.  Return a dictionary with all the requires variables
        to display the annual report to the landlord.
        """
        # Different categories
        expense_categories = ['Mortgage', 'Repairs', 'Utilities', 'Taxes', 'Insurance']

        # Calculate the sum of each category in the expense record
        total_expenses_by_category = {}
        for category in expense_categories:
            total_expenses_by_category[category] = self.expense_record.get_total_expenses_by_category(category)

        # Get total money made
        total_rental_income = self.rental_income_record.get_total_rental_income()

        # Get total money spent
        total_expenses = self.expense_record.get_total_expenses()

        # Calculate profit
        profit = total_rental_income - total_expenses

        return {
            'total_rental_income': total_rental_income,
            'total_expenses': total_expenses,
            'total_expenses_by_category': total_expenses_by_category,
            'profit': profit
        }