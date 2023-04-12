from tenant import Tenant
from rental_income import Rental_Income
from expense import Expense


class ApartmentBuilding:

    def __init__(self):
        self.tenants = []
        self.rental_incomes = {}
        self.expenses = []

    def add_tenant(self, apartment_number, tenant_name):
        new_tenant = Tenant(apartment_number, tenant_name)
        self.tenants.append(new_tenant)
        self.rental_incomes[apartment_number] = Rental_Income(apartment_number)

    def remove_tenant(self, apartment_number):
        self.tenants = [
            tenant for tenant in self.tenants if tenant.apartment_number != apartment_number]
        del self.rental_incomes[apartment_number]

    def record_rental_income(self, apartment_number, month, payment):
        self.rental_incomes[apartment_number].record_payment(month, payment)

    def record_expense(self, date, payee, amount, category):
        new_expense = Expense(date, payee, amount, category)
        self.expenses.append(new_expense)

    def generate_annual_report(self):
        total_income = sum(rental_income.get_total_income()
                           for rental_income in self.rental_incomes.values())
        expenses_by_category = defaultdict(float)
        for expense in self.expenses:
            expenses_by_category[expense.category] += expense.amount
        total_expenses = sum(expenses_by_category.values())
        net_profit = total_income - total_expenses

        return {
            "total_income": total_income,
            "expenses_by_category": expenses_by_category,
            "total_expenses": total_expenses,
            "net_profit": net_profit
        }
