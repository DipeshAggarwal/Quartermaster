init python:

    @property
    def get_current_tile():
        return map_data[y][x]

    @property
    def scouting_advantage():
        if store.scouted_this_tile:
            return True
        if roster.check_if_buff_exists("scout"):
            return True
        return False

    def enemy_movement():
        global enemy_location
        if enemy_turns_starts_at > day:
            return

        if enemy_location == (-1, -1):
            x, y = (0, 0)
        else:
            x, y = enemy_location

            if current_location[1] > enemy_location[1]:
                y += 1
            elif current_location[1] < enemy_location[1]:
                y -= 1
            else:
                x += 1

        enemy_location = (x, y)
        map_data[x][y].has_enemy_raided = True

        if enemy_location == current_location:
            renpy.jump("enemy_caught_with_player")

    def add_time(t):
        store.time += t
        if store.time > 23:
            store.time -= 24
            store.day += 1

    def add_day(d):
        store.day += 1
    
    def start_moving(scouting=False):
        renpy.hide_screen("chose_travel_mode_screen")

        store.scouted_this_tile = scouting
        x, y = current_location
        store.current_tile_type = base_layer_tiles[current_season][map_data[y][x].base_layer]
        map_data[y][x].has_player_visited = True
        enemy_movement()

        if map_data[y][x].has_enemy_raided:
            renpy.jump("stepped_on_a_raided_tile")
        renpy.jump("walk_to_new_tile_controller")

    def scouting_for_food():
        no_of_items = renpy.random.randint(0, 4)
        total_items = []

        for i in xrange(0, no_of_items):
            total_items.append(items_global_store.get_random_item)
        return total_items

    def get_raiding_party(members=3):
        total_members = 0
        for i in xrange(0, members):
            total_members.append(enemy_roster.get_random_enemy)

    def chooose_battle_party(members=3):
        pass
