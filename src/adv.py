from room import Room
from player import Player
from item import Item

items = {
     "Coins": Item("Coins", "Lost Treasure"),
     "Potato": Item("Potato", "Just a normal potato"),
     "Sword": Item("Sword", "Arawn's Mighty Blade")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons", [items["Sword"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["Potato"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! You see something shiny in the corner. The only exit is to the south.""", [items["Coins"]]),
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


new_player = Player("John Price", [], room['outside'])



ui_display = ""
ui_display += "\nActions: [get item] [drop item]  [i]nventory  [q]uit\n"
ui_display += "\nMovement: [n]orth  [s]outh  [e]ast  [w]est  \n"


directions = ("n", "s", "e", "w")

def err_msg():
    print(f"\nThat is not a valid input\n")
    print(new_player.current_room)

print("\n Enter n, s, e or w to navigate between rooms \n Enter 'get item' to pick up item, 'drop item' to get rid of it and 'i' to check your inventory\n Enter q to quit the game ")

while True:

    user_input = input("-").split()

    if len(user_input) == 1:
        if user_input[0] == "i":
            print(new_player)

        elif user_input[0] in directions:
            new_player.move(user_input[0])

        elif user_input[0] == "q":
            print("\nYou have quit the game\n")
            break
        
        else:
            err_msg()
            continue    


    elif len(user_input) == 2:
        if user_input[1] in items:
            new_player.action(user_input[0], items[user_input[1]])
        else:
            err_msg()
            continue    

    else:
        err_msg()
        continue    
