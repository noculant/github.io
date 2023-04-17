from tenant_class import Tenant
from rental_income_record_class import RentalIncomeRecord
from expense_record_class import ExpenseRecord
from annual_report_class import AnnualReport
from file_io import save_data, load_data

class Landlord:
    """
    Represents the top level class that connects everything together.  This is where the
    the list of tenants, income record, expense record, and annual record are stored and 
    accessed by the front end via Flask.
    """
    def __init__(self, tenant_filename='tenants.txt', rental_income_filename='rental_income_records.txt', expense_filename='expense_records.txt'):
        """
        Constructs the list of tenants, the rental income record, expense record, 
        and the annual report using data from the previous two.

        tenant_list: The list of tenant objects
        rental_income_record: The list of tenant payments to landlord
        expense_record: The list of payments the landlord made 
        annual_report: The annual report that calulates profit and categorical sums
        """
        self.tenant_filename = tenant_filename
        self.tenant_list = [Tenant(**tenant) for tenant in load_data(self.tenant_filename)]
        self.rental_income_record = RentalIncomeRecord(rental_income_filename)
        self.expense_record = ExpenseRecord(expense_filename)
        self.annual_report = AnnualReport(self.rental_income_record, self.expense_record)

    def add_tenant(self, aptNum, name, rate):
        """
        Appends a new tenant to the list of tenants

        aptNum: The apartment number
        name: The name of the tenant
        rate: The monthly rate for the apartment
        """
        new_tenant = Tenant(name, aptNum, rate)
        self.tenant_list.append(new_tenant)
        save_data(self.tenant_filename, [t.__dict__ for t in self.tenant_list])

    def record_rental_income(self, month, aptNum, amount):
        """
        Appends a new tenant to the list of tenants

        aptNum: The apartment number
        amount: The amount payed by tenant
        date: The date of the payment
        """
        self.rental_income_record.add_income(month, aptNum, amount)

    def record_expense(self, description, amount, date):
        """
        Appends a new tenant to the list of tenants

        description: The type of expense (mortgage, repairs, utilities, etc.)
        amount: The amount of the expense
        date: The date of the payment
        """
        self.expense_record.add_expense(description, amount, date)

    def generate_annual_report(self):
        """
        Calls the generate annual report function from the annual report
        class. Calculates the categorical sums, total expenses, total income, 
        and net profit.
        """
        return self.annual_report.generate_annual_report()
