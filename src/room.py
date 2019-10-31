# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    name: ''
    description: ''
    items: []

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def grab_item(self, item_name: str):
        itemToReturn: ''
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return item

    def __str__(self):
        string = f"{self.name}\n{self.description}"
        if len(self.items) > 0:
            string += "\n In the room you see \n"
            for item in self.items:
                string += item.__str__()

        return string
