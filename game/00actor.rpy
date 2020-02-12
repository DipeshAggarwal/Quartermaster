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

            self.status = "alive"

        def add_hp(self, change):
            self.health += change
            if self.health < 0:
                self.health = 0

        def hit(self):
            self.health -= 1
            if self.health < 1:
                self.status = "dead"

        def add_buff(self, buff):
            self.buffs.append(buff)
            if len(self.buffs) > 2:
                del self.buffs[0]

        def used_buff(self, buff):
            index = self.buffs.index(buff)
            del self.buffs[index]

        def is_buff_available(self, buff):
            if buff in self.buffs:
                return True
            else:
                return False

    class Enemy():

        def __init__(self, name, image, buff):
            self.name = name
            self.image = image
            self.buff = buff

    class Roster():

        def __init__(self):
            self.store = []

        def check_if_buff_exists(self, buff):
            for actor in self.store:
                if actor.is_buff_available(buff):
                    return True
            return False

        @property
        def get_random_enemy(self):
            index = renpy.random.randint(0, len(self.store))
            return self.store[index]
