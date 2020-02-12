init python:

    @property
    def get_raiding_party_buff():
        all_tags = []
        for raider in raiding_party:
            all_tags.append(raider.buff)
        return all_tags

    def get_raiding_party(members=3):
        raiding_party = []
        for i in xrange(0, members):
            raiding_party.append(enemy_roster.get_random_enemy)

    def chooose_battle_party(members=3):
        player_party = []
