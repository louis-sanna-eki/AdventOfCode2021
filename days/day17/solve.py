import math

file = open('days/day17/input.txt', 'r')
line = file.read()
file.close()

[raw_x_range, raw_y_range] = line.split(",")
[raw_x_range_min, raw_x_range_max] = raw_x_range.split("=")[1].split("..")
x_range_min = int(raw_x_range_min)
x_range_max = int(raw_x_range_max)
[raw_y_range_min, raw_y_range_max] = raw_y_range.split("=")[1].split("..")
y_range_min = int(raw_y_range_min)
y_range_max = int(raw_y_range_max)

print(x_range_min, x_range_max)
print(y_range_max, y_range_max)


def apply_step(probe):
    # assumes initial velocity is positive
    new_x_velocity = probe["x_velocity"] - 1 if probe["x_velocity"] > 0 else 0
    return dict({
        "x": probe["x"] + probe["x_velocity"],
        "y": probe["y"] + probe["y_velocity"],
        "x_velocity": new_x_velocity,
        "y_velocity": probe["y_velocity"] - 1
    })


def is_escaped(probe):
    x = probe["x"]
    y = probe["y"]
    if x > x_range_max:
        return True
    if y < y_range_min:
        return True
    return False


def is_in_range(probe):
    x = probe["x"]
    y = probe["y"]
    if x < x_range_min:
        return False
    if x > x_range_max:
        return False
    if y < y_range_min:
        return False
    if y > y_range_max:
        return False
    return True


def compute_max_y(probe):
    max_y = - math.inf
    while True:
        y = probe["y"]
        if y > max_y:
            max_y = y
        if is_in_range(probe):
            return max_y
        if is_escaped(probe):
            return -math.inf
        probe = apply_step(probe)


all_max_y = []
for x in range(0, x_range_max):
    for y in range(0, x_range_max):
        probe = dict({"x": 0, "y": 0, "x_velocity": x, "y_velocity": y})
        all_max_y.append(compute_max_y(probe))
result = max(all_max_y)

print(result)
