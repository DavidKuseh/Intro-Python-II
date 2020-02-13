# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description 

    def __str__(self):
        return f"\nYou are in the {self.name}: {self.description}\n"

    def wrong_room(self):
        print(f" You have entered the wrong room")