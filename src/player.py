# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, inventory, current_room):
        self.name = name
        self.inventory = inventory
        self.current_room = current_room

    def __str__(self):
        display_string = ""
        display_string += f"\nName:{self.name}\n"
        display_string += f"\nInventory:{[i.name for i in self.inventory]}"
        return display_string

    def move(self, direction):
        next_room  =  self.current_room.get_room_by_direction(direction)
        #check if move is valid
        if next_room:
            self.current_room = next_room
            print(self.current_room)
        else:
            return self.current_room.wrong_room()
    
    def action(self,action,item):
        if action == "get" and self.current_room.get_item(item):
            self.inventory.append(item) 
            print(item.on_take())
        elif action == "drop" and item in self.inventory:
            self.inventory.remove(item)
            self.current_room.items.append(item)
            print(item.on_drop())
            
        else:
            print(f"Im sorry {self.name}, you can't do that.")