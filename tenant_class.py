class Tenant:
    """
    Represents a tenant within the list of tenants.
    """
    def __init__(self, name, apartment_number, rate):
        """
        Constructs a tenant with a name, apartment number, and monthly rate.

        name: The name of the tenant
        apartment_number: The apartment number of the tenant
        rate: The monthly rate
        """
        self.name = name
        self.apartment_number = apartment_number
        self.rate = rate

