import csv
from itertools import combinations

test_data = []
data = []

with open('real_data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    test_data = list(reader)

for line in test_data:
    temp_line = []
    for num in line:
        temp_line.append(int(num))
    data.append(temp_line)


def all_ascending(line: list[int]) -> bool:
    for i in range(1, len(line)):
        if line[i] <= line[i - 1]:
            return False
    return True

def all_descending(line: list[int]) -> bool:
    for i in range(1, len(line)):
        if line[i] >= line[i - 1]:
            return False
    return True

def within_3(line: list[int]) -> bool:
    for i in range(1, len(line)):
        if abs(line[i] - line[i - 1]) > 3:
            return False
    return True

total_good_lines = 0
total_close_lines = 0

def enumerate_combinations(line: list[int]) -> list[list[int]]:
    lines = [list(item) for item in combinations(line, len(line) - 1)]
    return lines
    
    

for line in data:
    added = False
    if all_ascending(line) or all_descending(line):
        if within_3(line):
            total_good_lines += 1
            added = True
    combies = enumerate_combinations(line)
    for combination in combies:
        if all_ascending(combination) or all_descending(combination):
            if within_3(combination) and not added:
                added = True
                total_close_lines += 1
    



print(f"Problem 1: {total_good_lines}, Problem 2: {total_close_lines + total_good_lines}")