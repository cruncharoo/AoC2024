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
    loop = False
    while in_path and not loop:
        if [col,row, direction] in path:
            loop = True
            return loop
        
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
    return loop

def find_loops(map):
    loops = 0
    iter = 1
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(iter,loops)
            if map[i][j] == '.' and map[i][j] != '#':
                map_copy = deepcopy(map)
                map_copy[i] = map_copy[i][:j] + '#' + map_copy[i][j+1:]
                if find_path(map_copy):
                    loops += 1
            iter += 1
    return loops

print(find_loops(parsed_contents))