class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
    
    def __str__(self):
        return f"\n{self.name}"
    
    def look(self): 
        return f"{self.description}"

    def on_take(self):
        return f"You have picked up the {self.name}." 

    def on_drop(self):
        return f"You have dropped the {self.name}"