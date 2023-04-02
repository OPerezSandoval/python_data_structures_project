import csv
import datetime
import truck_class

from hash_map import HashMap
from package_class import Package

# This will read all the data inside the CSVfiles
with open("wgu_distances.csv") as dist_file:
    wgu_distances_file = list(csv.reader(dist_file))

with open("wgu_addresses.csv") as add_file:
    wgu_addresses_file = list(csv.reader(add_file))

with open("wgu_packages.csv") as pack_file:
    wgu_packages_file = list(csv.reader(pack_file))

# This will create a package object from the wgu_packages file and will
# load them into the hashmap
# Time complexity is O(n) where n is teh number of rows in file
def package_hashmap_load(filename, package_hash_map):
    with open(filename) as package_data:
        read_package_file = csv.reader(package_data)
        for row in read_package_file:
            package_ID_value = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            deadline_time = row[5]
            size = row[6]
            delivery_status = "At Hub"

            # This is the package object
            iterate_value = Package(package_ID_value, address, city, state, zipcode, deadline_time, size, delivery_status)

            # This will insert the data into the hash map
            package_hash_map.insert(package_ID_value, iterate_value)


# This method will look up the distance between two addresses
# Time complexity is O(1), where n is the number of rows in file
def addresses_distance(x_value, y_value):
    distance = wgu_distances_file[x_value][y_value]
    if distance == '':
        distance = wgu_distances_file[y_value][x_value]

    return float(distance)


# This method will iterate through the list of addresses and finds the address
# that matches the input string literal
# Time complexity is O(n) where n is the number of rows in the file
def retrieve_address(address):
    for row in wgu_addresses_file:
        if address in row[2]:
            return int(row[0])


# These will create all trucks and the packages that will be loaded on to it
# truck_a
truck_a = truck_class.Truck(16, 18, None, [1, 13, 14, 16, 19, 20, 15, 29, 30,
                                           8, 34, 37, 40, 7, 21, 4], 0.0,
                                           "4001 South 700 East",
                                           datetime.timedelta(hours=8))

# truck_b
truck_b = truck_class.Truck(16, 18, None, [3, 18, 36, 38, 6, 25, 28, 32, 31,
                                           26, 5, 17, 22, 11, 23, 12], 0.0,
                                           "4001 South 700 East",
                                           datetime.timedelta(hours=9, minutes=5))

# truck_c
truck_c = truck_class.Truck(16, 18, None, [9, 2, 10, 24, 27, 33, 35, 39], 0.0,
                                          "4001 South 700 East",
                                          datetime.timedelta(hours=10, minutes=20))

# This will create the HashMap
create_hash_map = HashMap()

# This will load the packages into the hashmap
package_hashmap_load("wgu_packages.csv", create_hash_map)

# This method uses the nearest neighbor approach to order the packages on a given truck
# It will cycle through the list of packages until none are leftover
# This method will  look up the distance to the nearest package and adds it to the
# trucks mileage attribute.
# Time complexity is O(n^2), where n is the total number of packages across all trucks
def nearest_neighbor_delivery(truck):

    packages_to_deliver = []
    for package_ID in truck.truck_packages:
        package = create_hash_map.get_hash_value(package_ID)
        packages_to_deliver.append(package)
    truck.truck_packages.clear()

    while len(packages_to_deliver) > 0:
        next_delivery = 2000
        next_package = None
        for package in packages_to_deliver:
            if addresses_distance(retrieve_address(truck.delivery_address),
                                  retrieve_address(package.delivery_address)) \
                                  <= next_delivery:

                next_delivery = addresses_distance(retrieve_address(truck.delivery_address),
                                                   retrieve_address(package.delivery_address))
                next_package = package
        truck.truck_packages.append(next_package.package_ID)
        packages_to_deliver.remove(next_package)
        truck.truck_mileage += next_delivery
        truck.delivery_address = next_package.delivery_address
        truck.time += datetime.timedelta(hours=next_delivery / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.start_time

# This will load the trucks
nearest_neighbor_delivery(truck_a)
nearest_neighbor_delivery(truck_b)

# This will make sure the a driver from the other trucks are able to go on truck c
truck_c.start_time = min(truck_a.time, truck_b.time)
nearest_neighbor_delivery(truck_c)

# Total milage for all trucks
total_milage = truck_a.truck_mileage + truck_b.truck_mileage + truck_c.truck_mileage