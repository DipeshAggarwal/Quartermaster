init python:

    class Actor():

        def __init__(self, name, morale, role, competence, buffs, health=5, hunger=0):
            self.name = name
            self.health = health
            self.morale = morale
            self.role = role
            self.competence = competence
            self.hunger = hunger
            self.buffs = []

        def add_hp(self, change):
            self.health += change
            if self.health < 0:
                self.health = 0

    class Enemy():

        def __init__(self, name, image, buff):
            self.name = name
            self.image = image
            self.buff = buff

    class Roster():

        def __init__(self):
            self.store = []

        @property
        def get_random_enemy(self):
            index = renpy.random.randint(0, len(self.store))
            return self.store[index]
