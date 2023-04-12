class AnnualReport:
    def __init__(self, rental_income_record, expense_record):
        self.rental_income_record = rental_income_record
        self.expense_record = expense_record

    def get_total_rental_income(self):
        return self.rental_income_record.get_total_rental_income()

    def get_total_expenses(self):
        return self.expense_record.get_total_expenses()

    def get_net_income(self):
        return self.get_total_rental_income() - self.get_total_expenses()

    def generate_annual_report(self):
        rental_income = self.get_total_rental_income()
        expenses = self.get_total_expenses()
        net_income = self.get_net_income()

        report = {
            "total_rental_income": rental_income,
            "total_expenses": expenses,
            "net_income": net_income
        }

        return report
