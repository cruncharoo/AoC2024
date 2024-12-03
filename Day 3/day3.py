
with open('real_data.txt', 'r') as file:
    data = file.read().splitlines()
    raw_data = list(data)

data_string = raw_data[0]

def find_valid_muls(data: str):
    indices = []
    index = data.find("mul(")
    while index != -1:
        indices.append(index)
        index = data.find("mul(", index + 1)
    
    valid_muls = []
    for index in indices:
        end_index = data.find(")", index)
        if end_index != -1:
            expression = data[index:end_index + 1]
            if expression.startswith("mul(") and expression.endswith(")"):
                try:
                    parts = expression[4:-1].split(",")
                    if len(parts) == 2 and all(part.strip().isdigit() for part in parts):
                        valid_muls.append(expression)
                except ValueError:
                    continue
    return valid_muls

def find_valid_muls_with_toggle(data: str):
    toggle = True
    filtered_data = ""
    i = 0
    while i < len(data):
        if data[i:i+7] == "don't()":
            toggle = False
            i = i + 7
        elif data[i:i+4] == "do()":
            toggle = True
            i = i + 4
        elif toggle:
            filtered_data += data[i]
            i += 1
        else:
            i += 1

    valid_muls = find_valid_muls(filtered_data)
    return valid_muls


def multiply_valid_muls(muls: list):
    result = 0
    for mul in muls:
        parts = mul[4:-1].split(",")
        result += int(parts[0].strip()) * int(parts[1].strip())
    return result

valid_muls = find_valid_muls_with_toggle(data_string)
print(valid_muls)
result = multiply_valid_muls(valid_muls)
print(result)

