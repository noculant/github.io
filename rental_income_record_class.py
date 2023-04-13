class RentalIncomeRecord:
    """
    Represents the list holding all of the payments from the tenants.
    """
    def __init__(self):
        """
        Constructs a list of tenant payment records.

        income_records: The list of payments from tenants
        """
        self.income_records = []

    def add_income(self, month, apartment_number, amount):
        """
        Appends a dictionary of data for each rental payment to
        the list.

        month: The month of the payment
        apartment_number: The apartment number of the tenant
        amount: The amount payed by the tenant
        """
        income = {
            "month": month,
            "apartment_number": apartment_number,
            "amount": amount
        }
        self.income_records.append(income)

    def get_total_income(self):
        """
        Calculates the total money made from the rental income record.
        """
        return sum(record['amount'] for record in self.income_records)
