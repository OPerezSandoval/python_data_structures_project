
# This will create a class for all the packages
class Package:
    # The init method initializes the instance variables
    # Time complexity is constant (O(1))
    def __init__(self, package_ID, delivery_address, delivery_city, delivery_state,
                 delivery_zipcode, delivery_deadline_time, package_weight, delivery_status):
        self.package_ID = package_ID
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_state = delivery_state
        self.delivery_zipcode = delivery_zipcode
        self.delivery_deadline_time = delivery_deadline_time
        self.package_weight = package_weight
        self.delivery_status = delivery_status
        self.departure_time = None
        self.delivery_time = None

    # The str method creates a formatted string of the object with iterations
    # Time complexity is linear (O(n))
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_ID, self.delivery_address,
                                                       self.delivery_city, self.delivery_state,
                                                       self.delivery_zipcode, self.delivery_deadline_time,
                                                       self.package_weight, self.delivery_time,
                                                       self.delivery_status)

    # The package_status method updates the status of the package
    # The time complexity is constant (O(1))
    def package_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.delivery_status = "Delivered"
        elif self.departure_time > convert_timedelta:
            self.delivery_status = "En route"
        else:
            self.delivery_status = "At Hub"