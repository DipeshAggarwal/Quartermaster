init python:

    class Inventory():

        def __init__(self):
            self.max_space = 0
            self.store = []

        def calculate_available_space(self):
            self.max_space = len(store.roster.store)

        def add_item(self, item):
            self.store.append(item)

        def use_item(self, item):
            index = self.store.index(item)
            del self.store[index]

screen inventory_screen():
    add Solid("#00000050")

    frame:
        background Solid("#ffffff")
        xysize(542, 646)
        xpos 34
        ypos 34
