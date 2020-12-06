file = open('map.txt', 'r')
map_basis = file.readlines()

def tree_count_for_slope(right_increment, down_increment):
    right_coordinate = 0
    down_coordinate = 0
    tree_count = 0
 
    while down_coordinate < len(map_basis):
        if is_tree_at_coordinates(right_coordinate, down_coordinate):
            tree_count += 1
        right_coordinate += right_increment
        down_coordinate += down_increment
        print("right" ,right_coordinate)
        print("down" ,down_coordinate)
 
    return tree_count

	
def is_tree_at_coordinates(hill_x, hill_y):
    map_x = hill_x % 31
    return map_basis[hill_y][map_x] == "#"
print(
    tree_count_for_slope(1, 1) *
    tree_count_for_slope(3, 1) *
    tree_count_for_slope(5, 1) * 
    tree_count_for_slope(7, 1) * 
    tree_count_for_slope(1, 2) 
)