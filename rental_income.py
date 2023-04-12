from collections import defaultdict


class Rental_Income:
    '''
    Represents a rental income record for a single apartment unit
    '''

    def __init__(self, apartmentNum):
        self.apartmentNum = apartmentNum
        self.monthly_payments = defauldict(float)

    '''
    Format the output when printing the class
    '''

    def __str__(self):
        return f"{self.apartmentNum}: {self.monthly_payments}"

    '''
    Record a single payment for a tenant for a specific month
    '''

    def recordPayment(self, month, payment):
        self.monthly_payments[month] += payment

    '''
    Calculates the total rental income from a single apartment unit
    '''

    def getTotalIncome(self):
        return sum(self.monthly_payments.values())
