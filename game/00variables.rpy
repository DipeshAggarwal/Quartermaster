default mid_layer_visible = False
default sky_layer_visible = False
default tile_in_x = 8
default tile_in_y = 6
default tile_width = 108
default tile_height = 108
default default_tilepath = "images/tiles/"

default current_turn_no = 0
default current_tile_type = ""
default enemy_turns_starts_at = 5

default time = 0

default current_location = (0, 0)
default next_location = (0, 0)
default scouted_this_tile = False
default current_season = "summer"

default map_data = [[MapTile(i, j) for i in range(0, tile_in_x)] for j in range(0, tile_in_y)]

default base_layer_tiles = {
    "summer": ["forest1", "forest2", "hill1", "hill2", "mnt1", "mnt2", "selo", "wild"]
}

# Don't change these variables
default recipe_book = RecipeBook()
default items_global_store = ItemStore()
default inventory = Inventory()
default roster = Roster()
default enemy_roster = Roster()