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
