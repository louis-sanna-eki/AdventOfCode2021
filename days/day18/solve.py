file = open('days/day18/input.txt', 'r')
lines = file.read().splitlines()
file.close()


def parse_number(raw_number):
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
        return dict({
            "left": parse_number(raw_left),
            "right": parse_number(raw_right),
        })
    return int(raw_number)


[line] = lines

print(parse_number(line))
