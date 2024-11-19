class Address:
    def __init__(self, number, street_name):
        self.number = number
        self.street_name = street_name

address = Address(123, "Main Street")
print(address.number, address.street_name)