# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, inventory, player_name):
        self.current_room = current_room
        self.inventory = inventory
        self.player_name = player_name

    def __repr__(self):
        return f"{self.player_name} is in {self.current_room}"
