### PLAYER MODULE

from room import Room
from item import Item


# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    current_room: ''
    item: []

    def __init__(self, current_room: Room):
        self.current_room = current_room
        self.items = []

    def change_room(self, room):
        self.current_room = room

    def get_room(self):
        return self.current_room

    def add_item(self, item: Item):
        self.items.append(item)

    def drop_item(self, item_name: str):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return item
        return None

    def __str__(self):
        string = self.current_room.__str__()
        if len(self.items) > 0:
            string += "\n You currently are carrying\n"
            for item in self.items:
                string += item.__str__() + "\n"

        return string
