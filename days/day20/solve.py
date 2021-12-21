file = open('days/day20/input.txt', 'r')
lines = file.read().splitlines()
file.close()

algorithm = lines[0]

raw_image = list(map(lambda line: list(line), lines[2:]))


def pad(array, padding="."):
    result = []
    initial_length = len(array)
    result.append([padding] * (initial_length + 2))
    for row in array:
        new_row = [padding] + row + [padding]
        result.append(new_row)
    result.append([padding] * (initial_length + 2))
    return result


def char_to_binary(char):
    if char == ".":
        return 0
    if char == "#":
        return 1
    raise NotImplementedError


def get(image, y, x, default='.'):
    if x < 0:
        return default
    if y < 0:
        return default
    if y >= len(image):
        return default
    if x >= len(image[y]):
        return default
    return image[y][x]


def compute_number(image, y, x, default):
    result = 0
    multiple = 8
    for delta_y in [-1, 0, 1]:
        for delta_x in [-1, 0, 1]:
            char = get(image, y + delta_y, x + delta_x, default)
            binary = char_to_binary(char)
            result += binary * 2**multiple
            multiple -= 1
    return int(result)


def enhance(image, default="."):
    result = [[0] * len(image) for _ in range(len(image))]
    for y in range(len(image)):
        for x in range(len(image[y])):
            number = compute_number(image, y, x, default)
            result[y][x] = algorithm[number]
    return result


def print_image(image):
    for row in image:
        print(row)


def count_lights(image):
    count = 0
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == "#":
                count += 1
    return count


def part_2():
    image = pad(pad(pad(pad(pad(raw_image)))))
    enhanced_image = enhance(image)
    for _ in range(1, 50):
        padded_enhanced = pad(enhanced_image, enhanced_image[0][0])
        enhanced_image = enhance(padded_enhanced, enhanced_image[0][0])
    result = count_lights(enhanced_image)
    print(result)


part_2()
