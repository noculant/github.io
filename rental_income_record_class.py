class RentalIncomeRecord:
    def __init__(self):
        self.income_records = []

    def add_income(self, month, apartment_number, amount):
        income = {
            "month": month,
            "apartment_number": apartment_number,
            "amount": amount
        }
        self.income_records.append(income)

    def get_total_income(self):
        return sum(record['amount'] for record in self.income_records)
