import random
import operator

    
world_size_x = int(input('Welcome! Now enter an integer. Your world should have size of: '))
world_size_y = int(input('Since we want it to be a 2D world, please enter another integer of your choice: '))


def generate_random_world(list_of_tiles, list_of_close_tiles, coordinates):
    random.seed()
    list_of_close_tiles.append(coordinates)
    for k in range(30):
        new_tile =(random.randint(0, world_size_x), random.randint(0, world_size_y))
        for tile in list_of_tiles:
            if new_tile[0] == tile [0]:
                if new_tile[1] == tile[1]:
                    break
            else:
                list_of_tiles.append(new_tile)
    return list_of_tiles


def sort_list_of_tiles_by_x_y(list_of_tiles):
    list_of_tiles = sorted(list_of_tiles, key=operator.itemgetter(0, 1))
    return list_of_tiles


def count_area(list_of_tiles, coordinates, list_of_close_tiles):
    print(list_of_close_tiles)
    for item in list_of_tiles:
        if item[0] == coordinates[0] or item[0] == coordinates[0] - 1 or item[0] == coordinates[0] + 1:
            if item[1] == coordinates[1] or item[1] == coordinates[1] - 1 or item[1] == coordinates[1] + 1:
                if item != coordinates:
                    list_of_close_tiles.append(item)
    return list_of_close_tiles
