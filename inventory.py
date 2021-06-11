# define class to manage video inventory and rentals
# rent_video()
# return_video()
# view_current_inventory()
# Update inventory.csv to store new changes, etc.
import csv
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
        pass
        # with open(".data/inventory.csv", "w") as data_file:
        #     header_data = ["id","title","rating","copies_available"]
        #     write_data = csv.DictWriter(data_file, fieldnames=header_data)
        #     for x in Inventory:
        #         print(x)
        #         write_data.writerow(x.__dict__)


    def return_video():
        pass

    @classmethod
    def view_current_inventory(cls):
        with open(path, 'r') as video_file:
            videos = csv.DictReader(video_file)
            video_list= []
            for video in videos:
                video_list.append(video)
                print(video)
            return video_list
