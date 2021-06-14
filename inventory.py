# define class to manage video inventory and rentals
# rent_video()
# return_video()
# view_current_inventory()
# Update inventory.csv to store new changes, etc.
import csv
from customer import Customer
from os import write
import os.path
from typing import TypeVar

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "data/inventory.csv")

class Inventory:
    def __init__(self, id, title, rating, copies_available ):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available
        
    @classmethod
    def rent_video(cls):
        title = input('Enter video ID or case sensitive title: ')
        customer_id = input('Please enter the customer ID for rental ')
        with open("data/inventory.csv", "r") as data_file:
            inventory_object = csv.reader(data_file)
            rental_list = []
            
            for x in inventory_object:
                rental_list.append(x)
            
            for sub_list in rental_list:
                
                if (title in sub_list[0]):
                    
                    print(sub_list, ' Video ID found!\n')
                    if sub_list[3] == '0':
                        print('No copies available.')
                        return False
                    else: 
                        sub_list[3] = eval(f"{sub_list[3]} - 1")
                        print('One copy rented to customer.')
                       
                elif (title in sub_list[1]):
                    print(sub_list, ' Video title found!\n')
                    if sub_list[3] == '0':
                        print('No copies available.')
                        return False
                    else:
                        sub_list[3] = eval(f"{sub_list[3]} - 1")
                        print('One copy rented to customer.')

        # with open("data/inventory.csv", 'w') as write_file:
        #     writer = csv.writer(write_file)
        #     writer.writerows(rental_list)

            # # update customer_list[3] and overwrite customers.csv
            # with open("data/customers.csv", "r") as data_file:
            #     customer_object = csv.reader(data_file)
            #     customer_list = []
            #     for customer in customer_object:
            #         customer_list.append(customer)
                
            # added_title = sub_list[1]
            # print(added_title, ' added title\n')
            # print(customer_id, ' customer ID\n')

            # for x in customer_list:
            #     if (customer_id in customer_list[-1]):
            #         print('WORK')
            #         customer_list[6][3] += str(f'added_title')
            # print(customer_list)

           



        

        


    # def return_video():
    #     pass

    # @classmethod
    # def view_current_inventory(cls):
    #     with open(path, 'r') as video_file:
    #         videos = csv.DictReader(video_file)
    #         video_list= []
    #         for video in videos:
    #             video_list.append(video)
    #             print(video)
    #         return video_list
