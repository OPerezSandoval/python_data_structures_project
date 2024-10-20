
# Omar Perez-Sandoval
# Student ID: 010213105
# Data Structures and Algorithms II
# NHP2 — NHP2 TASK 1: WGUPS ROUTING PROGRAM

import datetime

from algorithm import total_milage
from algorithm import create_hash_map


# This will create the class for the main program and user interface
class Main:
    print('*****************************')
    print("WGUPS Truck Delivery Program")
    print('*****************************')
    print('\nMiles to deliver all packages: ' + str(round(total_milage, 2)) + ' Miles')

    # This while loop will continue to run the program until user chooses to
    # exit, selecting option 3
    while True:
        user_input = input ("\nSelect an option:" 
                    "\n 1 - Track an Individual Package" 
                    "\n 2 - View Delivery Status at a Given Time " 
                    "\n 3 - Exit the program" 
                    "\nEnter option: ")

        # This will ask the user for a package id, and if it is valid it
        # will ask for a time, then it will output the package info
        if user_input == "1":
            try:
                while True:
                    package_id_input = input("Enter the package ID: ")
                    if int(package_id_input) <= 41:
                        package = create_hash_map.get_hash_value(int(package_id_input))
                        user_time = input("Enter a time in the following format, HH:MM:SS ")
                        (h, m, s) = user_time.split(":")
                        convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        package.package_status(convert_timedelta)
                        print("\nPackageID | Address | City | ST | Zip | Deadline Time | Weight | Delivered Time | Status")
                        print(str(package))
                        break
                    else:
                        print("Please enter a valid package id!")
                        continue
            except ValueError:
                print("\nTime format is not correct!")

        # This will ask user to input a valid time to check deliveries
        # If the user does not input correct format the program will reset
        elif user_input == "2":
            try:

                user_time = input("Enter a time in the following format, HH:MM:SS ")
                (h, m, s) = user_time.split(":")
                convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m),
                                                       seconds=int(s))

                for packageID in range(1, 41):
                    package = create_hash_map.get_hash_value(packageID)
                    package.package_status(convert_timedelta)
                    print("\nPackageID | Address | City | ST | Zip | Deadline Time | Weight | Delivered Time | Status")
                    print(str(package))
            except ValueError:
                print("\nTime format is not correct!")

        # This will exit the program if user inputs 3
        elif user_input == "3":
            print("\nUser choose to exit program!")
            exit()

        # This will catch all other errors and continue the program
        else:
            print("\nPlease enter a valid option!")
            continue
