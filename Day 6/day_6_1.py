from copy import deepcopy

def parse_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        # Add your parsing logic here
        parsed_contents = contents.splitlines()  # Example: split contents into lines
    return parsed_contents

parsed_contents = parse_file('real_input.txt')

def find_carrot(map):
    col = 0
    row = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != '.' and map[i][j] != '#':
                row = i
                col = j
                carrot = map[row][col]
    if carrot == 'v':
        direction = 'down'
    elif carrot == '^':
        direction = 'up'
    elif carrot == '>':
        direction = 'right'
    elif carrot == '<':
        direction = 'left'
    return col, row, direction

def find_path(map):
    col,row, direction = find_carrot(map)
    map[row] = map[row][:col] + '.' + map[row][col+1:]
    path = []
    in_path = True
    while in_path:
        match direction:
            case 'up':        
                if row-1 < 0:
                    in_path = False
                    path.append([col,row, direction])
                elif map[row-1][col] == '#':
                    direction = 'right'
                elif map[row-1][col] == '.':
                    path.append([col,row, direction])
                    row -= 1
            case 'down':
                if row+1 >= len(map):
                    in_path = False
                    path.append([col,row, direction])
                elif map[row+1][col] == '#':
                    direction = 'left'
                elif map[row+1][col] == '.':
                    path.append([col,row, direction])
                    row += 1
            case 'right':
                if col+1 >= len(map[col]):
                    in_path = False
                    path.append([col,row, direction])
                elif map[row][col+1] == '#':
                    direction = 'down'
                elif map[row][col+1] == '.':
                    path.append([col,row, direction])
                    col += 1
            case 'left':
                if col-1 < 0:
                    in_path = False
                    path.append([col,row, direction])
                elif map[row][col-1] == '#':
                    direction = 'up'
                elif map[row][col-1] == '.':
                    path.append([col,row, direction])
                    col -= 1
    return path

good_path = find_path(parsed_contents)
print(good_path, len(good_path))

new_map = deepcopy(parsed_contents)
for _ in good_path:
    col,row,direction = _
    new_map[row] = new_map[row][:col] + 'X' + new_map[row][col+1:]

unique_locations = []
for move in good_path:
    location = [move[0], move[1]]
    if location not in unique_locations:
        unique_locations.append(location)

print(len(unique_locations))
