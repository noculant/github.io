class RentalIncomeRecord:
    def __init__(self):
        self.income_records = {}

    def add_income(self, apartment_number, month, amount):
        if apartment_number not in self.income_records:
            self.income_records[apartment_number] = {}

        self.income_records[apartment_number][month] = amount

    def get_income(self, apartment_number, month):
        if apartment_number in self.income_records and month in self.income_records[apartment_number]:
            return self.income_records[apartment_number][month]
        return None

    def get_total_income(self, apartment_number):
        if apartment_number in self.income_records:
            return sum(self.income_records[apartment_number].values())
        return None

    def get_monthly_income(self, month):
        monthly_income = 0
        for apartment_number in self.income_records:
            if month in self.income_records[apartment_number]:
                monthly_income += self.income_records[apartment_number][month]
        return monthly_income
