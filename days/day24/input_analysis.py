
################## Machine state ########################
w = 0
x = 0
y = 0
z = 0

################## python translation of first sequence########################

inputs = list([])


# inp w
w = inputs[0]
# mul x 0
# add x z
# mod x 26
# div z 1
# add x 12
x = z % 26 + 12
# eql x w
# eql x 0
x = 1 if x != w else 0
# mul y 0
# add y 25
# mul y x
# add y 1
y = 25 * x + 1  # y = 1
# mul z y
z *= y  # z = z
# mul y 0
# add y w
# add y 6
# mul y x
y = (w + 6) * x  # y = 0
# add z y
z += y  # z = z

if (w == z % 26 + 12):
    z = z
else:
    z = 26  # looks false...

################## python translation of second sequence########################

p = 1
q = 11
r = 12

# inp w
w = inputs[1]
# mul x 0
# add x z
# mod x 26
# add x q
x = z % 26 + q
# div z p
z = z / p
# eql x w
# eql x 0
x = 1 if z % 26 + q != w else 0  # x = 1 if x != w else 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y r
# mul y x
# add z y

if z % 26 + q != w:  # x = 1 # z = z / p
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    z = 26 * (z/p)
    # mul y 0
    # add y w
    # add y r
    # mul y x
    y = w + r
    # add z y
    z = 26 * (z/p) + w + r

if z % 26 + q == w:  # x = 0 # z = z/p
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    z = z  # = z/p
    # mul y 0
    # add y w
    # add y r
    # mul y x
    y = 0
    # add z y
    z = z/p

# Final conversion

if z % 26 + q == w:
    z = z/p
else:
    z = 26 * (z/p) + w + r
