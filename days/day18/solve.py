file = open('days/day18/input.txt', 'r')
lines = file.read().splitlines()
file.close()


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
    return dict({
        "parent": parent,
        "left": None,
        "right": None,
        "value": int(raw_number)
    })


def number_to_string(number):  # helper function for testing
    if number["value"] is not None:
        return str(number["value"])
    result = "[" + number_to_string(number["left"]) + \
        "," + number_to_string(number["right"]) + "]"
    return result


def find_with_left_dfs(number, check_condition, level=0):
    if check_condition(number, level):
        return number
    found_on_left = find_with_left_dfs(
        number["left"], check_condition, level+1)
    if found_on_left is not None:
        return found_on_left
    found_on_right = find_with_left_dfs(
        number["right"], check_condition, level+1)
    if found_on_right is not None:
        return found_on_right
    return None


def should_explode(node, level):
    if level >= 4:
        return True
    return False


def find_number_to_explode(number):
    return find_with_left_dfs(number, should_explode)


def isLeft(node):
    return node["parent"]["left"] == node


def reduce(number):
    return number
