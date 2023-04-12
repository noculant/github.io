class Tenant:
    def __init__(self, name, apartment_number, rate):
        self.name = name
        self.apartment_number = apartment_number
        self.rate = rate

    def get_name(self):
        return self.name

    def get_apartment_number(self):
        return self.apartment_number

    def get_rate(self):
        return self.rate

    def set_name(self, name):
        self.name = name

    def set_rate(self, rate):
        self.rate = rate
