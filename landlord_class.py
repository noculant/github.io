from tenant_class import Tenant
from rental_income_record_class import RentalIncomeRecord
from expense_record_class import ExpenseRecord
from annual_report_class import AnnualReport

class Landlord:
    def __init__(self):
        self.tenant_list = []
        self.rental_income_record = RentalIncomeRecord()
        self.expense_record = ExpenseRecord()
        self.annual_report = AnnualReport(self.rental_income_record, self.expense_record)

    def add_tenant(self, apartment_number, name, rate):
        new_tenant = Tenant(apartment_number, name, rate)
        self.tenant_list.append(new_tenant)

    def record_rental_income(self, apartment_number, amount, date):
        self.rental_income_record.add_income(apartment_number, amount, date)

    def record_expense(self, description, amount, date):
        self.expense_record.add_expense(description, amount, date)

    def get_annual_report(self, year):
        return self.annual_report.get_report(year)
