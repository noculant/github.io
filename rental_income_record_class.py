from tenant_class import Tenant
from expense_record_class import ExpenseRecord
from annual_report_class import AnnualReport
from file_io import save_data, load_data

class RentalIncomeRecord:
    """
    Represents the list holding all of the payments from the tenants.
    """
    def __init__(self, rental_income_filename='rental_income_records.txt'):
        """
        Constructs a list of tenant payment records.

        income_records: The list of payments from tenants
        """
        self.rental_income_filename = rental_income_filename
        self.rental_income_records = load_data(self.rental_income_filename)


    def add_income(self, month, apartment_number, amount):
        """
        Appends a dictionary of data for each rental payment to
        the list.

        month: The month of the payment
        apartment_number: The apartment number of the tenant
        amount: The amount payed by the tenant
        """
        income = {
            "apartment_number": apartment_number,
            "date": month,
            "amount": amount
            
        }
        self.rental_income_records.append(income)
        save_data(self.rental_income_filename, self.rental_income_records)

    def get_total_income(self):
        """
        Calculates the total money made from the rental income record.
        """
        return sum(record['amount'] for record in self.rental_income_records)
