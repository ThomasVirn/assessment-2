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

        with open("data/customers.csv", "r") as data_file:
            customer_object = csv.reader(data_file)
            customer_id = input('Please enter your customer ID: ')
            customer_list = []
            for customer in customer_object:
                customer_list.append(customer)
            print(customer_list)
            for customer in customer_list:
                if (customer_id in customer[0]):
                    print(f'{customer[1]} currently has {customer[3]} rented')



    def add_customer():
        print("-- Enter New Customer Information Below --")
    
        first_name = input('Enter first name of customer: ')
        last_name = input('Enter last name of customer: ')

        with open("data/customers.csv", "r") as data_file:
            customer_object = csv.reader(data_file)
            customer_list = []

            for customer in customer_object:
                customer_list.append(customer)

            id_num = (int(customer_list[-1][0]) + 1)
            new_customer = [id_num,first_name, last_name, '']
            customer_list.append(new_customer)
            print(f'\nCustomer {new_customer[1]} added!')

            with open("data/customers.csv", 'w') as write_file:
                writer = csv.writer(write_file)
                writer.writerows(customer_list)

    
 

    

