# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory
# class Room(Item):
#     def __init__(self, room_name, room_description, item_name, item_description):
#         super().__init__(room_name, room_description)
#         self.room_name = room_name
#         self.room_description = room_description

    def __repr__(self):
        return f"{self.name}, {self.description}"
