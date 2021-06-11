# def class for utilizing customer info
# methods include...
# view_rentals() (arguments will be by customer ID)
# add_customer (adds customer to database, all headers will be args, must create unique ID for each customer)
# Update customers.csv to store new changes, etc.

import csv
import os.path
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "data/customers.csv")

class Customer:
    def __init__(self, id, first_name, last_name, current_video_rentals):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    def view_rentals():
        pass

    def add_customer():
        pass

    

