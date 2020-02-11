init python:

    class MapTile():

        def __init__(self, x, y):
            self.x = x
            self.y = y

            self.base_layer = renpy.random.randint(0, 7)
            self.mid_layer = renpy.random.randint(0, 7)
            self.sky_layer = renpy.random.randint(0, 7)
            self.security_rating = renpy.random.randint(0, 20)
            self.searching_rating = renpy.random.randint(0, 30)

        @property
        def base_image(self):
            return "base/" + store.base_layer_tiles[current_season][self.base_layer] + ".jpg"

        @property
        def mid_image(self):
            return "mid/" + store.base_layer_tiles[current_season][self.base_layer] + ".jpg"

        @property
        def sky_image(self):
            return "sky/" + store.base_layer_tiles[current_season][self.base_layer] + ".jpg"

screen map_overlay(filepath=None):
    if filepath:
        default path = filepath
    else:
        default path = default_tilepath

    for y in xrange(tile_in_y):
        for x in xrange(tile_in_x):
            add path + map_data[y][x].base_image xpos x*tile_width ypos y*tile_height

            if mid_layer_visible:
                add path + mid_image[y][x].base_image xpos x*tile_width ypos y*tile_height
            if sky_layer_visible:
                add path + sky_image[y][x].base_image xpos x*tile_width ypos y*tile_height

    fixed:
        xysize (108, 108)
        xpos current_location[0]*tile_width
        ypos current_location[1]*tile_height

        add "images/pin.png" xalign 0.5 yalign 0.5

    if current_location[0] > 0:
        $ x = (current_location[0] - 1) * tile_width
        $ y = current_location[1] * tile_height
        imagebutton:
            idle "tiles/ui/blank.png"
            hover "tiles/ui/blank_hover.png"

            action SetVariable("next_location", (current_location[0]-1, current_location[1])), Show("chose_travel_mode_screen")
            pos (x, y)

    if current_location[1] > 0:
        $ x = current_location[0] * tile_width
        $ y = (current_location[1] - 1) * tile_height
        imagebutton:
            idle "tiles/ui/blank.png"
            hover "tiles/ui/blank_hover.png"

            action SetVariable("next_location", (current_location[0], current_location[1]-1)), Show("chose_travel_mode_screen")
            pos (x, y)

    if current_location[0] < tile_in_x-1:
        $ x = (current_location[0] + 1) * tile_width
        $ y = current_location[1] * tile_height
        imagebutton:
            idle "tiles/ui/blank.png"
            hover "tiles/ui/blank_hover.png"

            action SetVariable("next_location", (current_location[0]+1, current_location[1])), Show("chose_travel_mode_screen")
            pos (x, y)

    if current_location[1] < tile_in_y-1:
        $ x = current_location[0] * tile_width
        $ y = (current_location[1] + 1) * tile_height
        imagebutton:
            idle "tiles/ui/blank.png"
            hover "tiles/ui/blank_hover.png"

            action SetVariable("next_location", (current_location[0], current_location[1]+1)), Show("chose_travel_mode_screen")
            pos (x, y)

screen chose_travel_mode_screen():
    modal True
    add Solid("#00000050")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15

        textbutton _("Slower with scouting") action Function(start_moving, scouting=True)
        textbutton _("Faster with the risk of ambush") action Function(start_moving, scouting=False)

label walk_to_new_tile_controller:
    "Here goes the logic for controlling events showcase and what happens while walking to a new tile."

    $ current_location = next_location
    jump new_tile_controller

label new_tile_controller:
    "Here goes the logic for controlling events showcase and what happens on a new tile."
    call screen map_overlay
