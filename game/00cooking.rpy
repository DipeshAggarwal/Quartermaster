init python:

    class ItemStore():

        def __init__(self):
            self.store = {}

        def load(self, filepath="items"):
            file_list = load(filepath, "index")

            for file in file_list:
                data = load(filepath, file)
                self.store[data["id"]] = Item(**data)

        @property
        def get_random_item(self):
            return renpy.random.choice(self.store.keys)

    class Item():

        def __init__(self, id, name, image, description, cost, buff, stackable=True):
            self.id = id
            self.name = name
            self.image = image
            self.description = description
            self.cost = cost
            self.buff = buff
            self.stackable = stackable

    class RecipeBook():

        def __init__(self):
            self.store = {}

        def load(self, filepath="recipes"):
            return
            file_list = load(filepath, "index")

            for file in file_list:
                data = load(filepath, file)
                ing = ",".join(sorted(data["ingredients"]))
                self.store[ing] = Recipe(**data)

        def add_to_log(self, ing, recipe):
            ing = sorted(ing)
            self.store[set(ing)] = recipe

        def is_valid_recipe(self, ing_1, ing_2):
            key = ",".join(sorted([ing_1, ing_2]))
            if key in self.store:
                self.store[key].cook()
            else:
                return 0

    class Recipe():

        def __init__(self, id, name, image, description, ingredients, heals, time_needed, cooking_location, random_cooking_chance, produces):
            self.id = id
            self.name = name
            self.image = image
            self.description = description
            self.ingredients = ingredients
            self.heals = heals
            self.time_needed = time_needed
            self.cooking_location = cooking_location
            self.random_cooking_chance = random_cooking_chance
            self.produces = produces

            self.times_cooked = 0

        def cook(self):
            for ing in self.ingredients:
                store.inventory.use_item(ing)
            store.inventory.add_item(self.produces)
