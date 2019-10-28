### PLAYER MODULE

from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    current_room: ''

    def __init__(self, current_room: Room):
        self.current_room = current_room

    def change_room(self, room):
        self.current_room = room

    def get_room(self):
        return self.current_room
