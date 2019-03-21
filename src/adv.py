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

# Make a new player object that is currently in the 'outside' room.


player = Player(room['outside'], [])
print(player)


# def grab_item(item):
#     try:
#         player.inventory.index(item)
#         player.inventory.remove(item)
#         player.inventory.append(item)
#     except:
#         print(item, "is not here!")


def take_from_room(item, current_room):
    try:
        location = current_room.split(' ')[0].lower()
        room[location].inventory.remove(item)
        player.inventory.append(item)
        print("Player inventory:", player.inventory)
        print("Room inventory:", room[location].inventory)

    except:
        print(item, "is not here!")


def drop_item(item, current_room):
    try:
        location = current_room.split(' ')[0].lower()
        print("Pre drop Player inventory:", player.inventory)
        print("Pre drop Room inventory:", room[location].inventory)
        player.inventory.remove(item)
        room[location].inventory.append(item)
        print("Player inventory:", player.inventory)
        print("Room inventory:", room[location].inventory)

    except:
        print(item, "is not here - nothing to drop!")


def try_direction(direction, current_room):
    attribute = direction + "_to"

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)


# Write a loop that:
#
while True:
    # * Prints the current room name
    print(player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    # Prints items
    print(player.current_room.inventory)
    # * Waits for user input and decides what to do.
    # s = input("\n>").lower()[0]
    s = input("\n>").lower().split(' ')
    print("First s =", len(s))
    if len(s) == 1:
        # grab the first character of the first word
        s = s[0][0]
        print("Second s =", s)
        if s == "q":
            print("See you next time!")
            break

        elif s == "i":
            print("Player inventory:", player.inventory)
            # continue

        else:
            player.current_room = try_direction(s, player.current_room)

    elif len(s) == 2:
        first_word = s[0]
        print("First word=", first_word)
        second_word = s[1]
        if (first_word == "get" or first_word == "take"):
            print("Yeahhh", first_word)
            print("Second word =>", second_word)
            print("Inventory", player.current_room.inventory)
            if (second_word in player.current_room.inventory):
                print("It's in there!!")
                take_from_room(second_word, player.current_room.name)
                Item.on_take(second_word)
            else:
                print(second_word, "is not here!")
        elif (first_word == 'drop'):
            drop_item(second_word, player.current_room.name)
        else:
            print("You must get, take  or drop!")
        continue

    else:
        print("I don't understand that.")
        continue

        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.

        #
        # If the user enters "q", quit the game.
