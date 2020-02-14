# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description 
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def get_room_by_direction(self,direction):
        print(direction)
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        else: 
            return None
    
    def get_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        else:
            print("That item is not here.")
            return False


    def __str__(self):
        return f"\n{self.name}\n{self.description}\n\nRoom Items {[i.name for i in self.items]}"
    def wrong_room(self):
        print(f"\nYou cannot enter that room\n\n{self.description}\n")