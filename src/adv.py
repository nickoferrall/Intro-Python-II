from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['coffee']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['bottle']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

item = {
    'bottle': Item("bottle", "the bottle is old"),
    'coffee': Item('coffee', 'from Brazil')
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# room names
names = ['outside', 'foyer', 'overlook', 'narrow', 'treasure']

# intro message
print("\nWelcome. May the odds forever be in your favour. \n")

player_name = input("\n> What is your name?\n\n")

# make a new player object that is currently in the 'outside' room.
player = Player(room['outside'], [], player_name)
print("\n", player)


# get the inventory from a room
def get_room_inventory(current_room):
    try:
        location = current_room.split(' ')[0].lower()
        if location in names:
            return room[location].inventory
        elif current_room.split(' ')[1].lower() in names:
            location = current_room.split(' ')[1].lower()
            return room[location].inventory
    except:
        print(current_room, "does not exist!")


# take the item from the room and add it to player inventory
def take_from_room(item, current_room):
    try:
        location = current_room.split(' ')[0].lower()
        room[location].inventory.remove(item)
        player.inventory.append(item)

    except:
        print(item, "is not here!")


# drop the item from player inventory into the room
def drop_item(item, current_room):
    try:
        location = current_room.split(' ')[0].lower()
        player.inventory.remove(item)
        room[location].inventory.append(item)
    except:
        print(item, "is not here - nothing to drop!")


# move the player into a different room
def try_direction(direction, current_room):
    attribute = direction + "_to"
    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)


# Write a loop that:
#
while True:
    s = input(
        "\n>Make your move. Choose North, South, East or West or get / drop items.\n\n").lower().split(' ')
    if len(s) == 1:
        # grab the first character of the first word
        s = s[0][0]
        if s == "q":
            print("See you next time!")
            break

        elif s == "i":
            print("Player inventory:", player.inventory)

        else:
            player.current_room = try_direction(s, player.current_room)
            if player.current_room != None:
                print(player.current_room)
                room_inventory = get_room_inventory(player.current_room.name)
                print("Inventory in the room:", room_inventory)
            else:
                print("\n\n--------Muerto--------\n\n")
                break

    elif len(s) == 2:
        first_word = s[0]
        second_word = s[1]
        if (first_word == "get" or first_word == "take"):
            if (second_word in player.current_room.inventory):
                take_from_room(second_word, player.current_room.name)
                Item.on_take(second_word)
            else:
                print(second_word, "is not here!")
        elif (first_word == 'drop'):
            drop_item(second_word, player.current_room.name)
            Item.on_drop(second_word)
        else:
            print("You must get, take or drop!")
        continue

    else:
        print("I don't understand that.")
        continue
