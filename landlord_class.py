from tenant_class import Tenant
from rental_income_record_class import RentalIncomeRecord
from expense_record_class import ExpenseRecord
from annual_report_class import AnnualReport

class Landlord:
    """
    Represents the top level class that connects everything together.  This is where the
    the list of tenants, income record, expense record, and annual record are stored and 
    accessed by the front end via Flask.
    """
    def __init__(self):
        """
        Constructs the list of tenants, the rental income record, expense record, 
        and the annual report using data from the previous two.

        tenant_list: The list of tenant objects
        rental_income_record: The list of tenant payments to landlord
        expense_record: The list of payments the landlord made 
        annual_report: The annual report that calulates profit and categorical sums
        """
        self.tenant_list = []
        self.rental_income_record = RentalIncomeRecord()
        self.expense_record = ExpenseRecord()
        self.annual_report = AnnualReport(self.rental_income_record, self.expense_record)

    def add_tenant(self, aptNum, name, rate):
        """
        Appends a new tenant to the list of tenants

        aptNum: The apartment number
        name: The name of the tenant
        rate: The monthly rate for the apartment
        """
        new_tenant = Tenant(aptNum, name, rate)
        self.tenant_list.append(new_tenant)

    def record_rental_income(self, aptNum, amount, date):
        """
        Appends a new tenant to the list of tenants

        aptNum: The apartment number
        amount: The amount payed by tenant
        date: The date of the payment
        """
        self.rental_income_record.add_income(aptNum, amount, date)

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
