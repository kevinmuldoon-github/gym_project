# Define the activity class for gym classes

from sqlite3 import DateFromTicks


class Activity:
    def __init__(self, type, date,time, id = None):
        self.type = type
        self.date = date
        self.time = time
        self.id = id