
# This will create a class for the trucks
class Truck:
    # The init method initializes the instance variables
    # Time complexity is constant (O(1))
    def __init__(self, truck_space, truck_speed, truck_load, truck_packages,
                 truck_mileage, delivery_address, start_time):
        self.truck_space = truck_space
        self.truck_speed = truck_speed
        self.truck_load = truck_load
        self.truck_packages = truck_packages
        self.truck_mileage = truck_mileage
        self.delivery_address = delivery_address
        self.start_time = start_time
        self.time = start_time

    # The str method creates a formatted string of the object with iterations
    # Time complexity is linear (O(n))
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.truck_space, self.truck_speed,
                                               self.truck_load, self.truck_packages,
                                               self.truck_mileage,self.delivery_address,
                                               self.start_time)