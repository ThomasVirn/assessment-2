# interface to access all methods for managing customer info and inventory control
# has to be able to qut() once done
# #  Welcome to Code Platoon Video!
# 1. View video inventory
# 2. View customer's rented videos
# 3. Rent video
# 4. Return video
# 5. Add new customer
# 6. Exit

from customer import Customer
from inventory import Inventory
import csv
import os.path

class Interface:
    def __init__(self):
        pass

    def main_menu(self):
        return int(input(f"""
       1. View video inventory
       2. View customer's rented videos
       3. Rent video
       4. Return video
       5. Add new customer
       6. Exit
     """))

    def menu_selection(self):
        print("""
       Welcome to Code Platoon Video! 
       """)
        input = self.main_menu()
        while True == True:
            if input == 1:
                Inventory.view_current_inventory()
                break
            elif input == 2:
                Customer.view_rentals()
                break
            elif input == 3:
                Inventory.rent_video()
                break
            elif input == 4:
                Inventory.return_video()
                break
            elif input == 5:
                Customer.add_customer()
                break
            elif input == 6:
                quit()
                

           
       