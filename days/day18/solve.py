import math

file = open('days/day18/input.txt', 'r')
lines = file.read().splitlines()
file.close()


def build_natural_number(value, parent):
    return dict({
        "parent": parent,
        "left": None,
        "right": None,
        "value": value
    })


def parse_number(raw_number, parent=None):
    if raw_number[0] == "[":
        index = 0
        unmatched_bracket_count = 0
        comma_index = None
        while True:
            index += 1
            if raw_number[index] == "[":
                unmatched_bracket_count += 1
            if raw_number[index] == "]":
                unmatched_bracket_count -= 1
            if raw_number[index] == "," and unmatched_bracket_count == 0:
                comma_index = index
                break

        raw_left = raw_number[1:comma_index]
        raw_right = raw_number[comma_index+1:-1]
        number = dict({
            "parent": parent,
            "left": parse_number(raw_left),
            "right": parse_number(raw_right),
            "value": None
        })
        number["left"] = parse_number(raw_left, number)
        number["right"] = parse_number(raw_right, number)
        return number
    return build_natural_number(int(raw_number), parent)


def number_to_string(number):  # helper function for testing
    if number["value"] is not None:
        return str(number["value"])
    result = "[" + number_to_string(number["left"]) + \
        "," + number_to_string(number["right"]) + "]"
    return result


def find_with_left_dfs(number, check_condition, level=0):
    if check_condition(number, level):
        return number
    if number["value"] is not None:
        return None
    found_on_left = find_with_left_dfs(
        number["left"], check_condition, level+1)
    if found_on_left is not None:
        return found_on_left
    found_on_right = find_with_left_dfs(
        number["right"], check_condition, level+1)
    if found_on_right is not None:
        return found_on_right
    return None


def find_with_right_dfs(number, check_condition, level=0):
    if check_condition(number, level):
        return number
    found_on_right = find_with_right_dfs(
        number["right"], check_condition, level+1)
    if found_on_right is not None:
        return found_on_right
    found_on_left = find_with_right_dfs(
        number["left"], check_condition, level+1)
    if found_on_left is not None:
        return found_on_left
    return None


def should_explode(node, level):
    if node is None:
        return False
    if node["value"] is not None:
        return False
    if level >= 4:
        return True
    return False


def find_number_to_explode(number):
    return find_with_left_dfs(number, should_explode)


def should_split(node, level):
    if node is None:
        return False
    if node["value"] is None:
        return False
    return node["value"] >= 10


def find_number_to_split(number):
    return find_with_left_dfs(number, should_split)


def is_left(node):
    return node["parent"]["left"] is node


def is_right(node):
    return node["parent"]["right"] is node


def find_left_neighbor(number, check_condition):
    if number["parent"] is None:
        return None
    if is_right(number):
        return find_with_right_dfs(number["parent"]["left"], check_condition)
    return find_left_neighbor(number["parent"], check_condition)


def find_right_neighbor(number, check_condition):
    if number["parent"] is None:
        return None
    if is_left(number):
        return find_with_left_dfs(number["parent"]["right"], check_condition)
    return find_right_neighbor(number["parent"], check_condition)


def is_natural(number, level):
    if number["value"] is not None:
        return True
    return False


def explode(number):
    left_value = number["left"]["value"]
    right_value = number["right"]["value"]
    natural_left = find_left_neighbor(number, is_natural)
    if natural_left is not None:
        natural_left["value"] += left_value
    natural_right = find_right_neighbor(number, is_natural)
    if natural_right is not None:
        natural_right["value"] += right_value
    number["right"] = None
    number["left"] = None
    number["value"] = 0


def split(number):
    value = number["value"]
    number["left"] = build_natural_number(math.floor(value/2), number)
    number["right"] = build_natural_number(math.ceil(value/2), number)
    number["value"] = None


def reduce(number):
    while True:
        number_to_explode = find_number_to_explode(number)
        if number_to_explode is not None:
            explode(number_to_explode)
            continue
        number_to_split = find_number_to_split(number)
        if number_to_split is not None:
            split(number_to_split)
            continue
        break
    return number


def add(number_1, number_2):
    joined_numbers = dict({
        "parent": None,
        "left": number_1,
        "right": number_2,
        "value": None
    })
    number_1["parent"] = joined_numbers
    number_2["parent"] = joined_numbers
    return reduce(joined_numbers)


def magnitude(number):
    if number["value"] is not None:
        return number["value"]
    return 3 * magnitude(number["left"]) + 2 * magnitude(number["right"])


number_sum = parse_number(lines[0])
for index in range(1, len(lines)):
    number = parse_number(lines[index])
    number_sum = add(number_sum, number)

result = magnitude(number_sum)

print(result)
