from z3 import And, If, Int, Optimize

file = open('days/day24/input.txt', 'r')
lines = file.read().splitlines()
file.close()

CONSTRAINT_LENGTH = 18

constraints = list()
for contraint_index in range(0, int(len(lines) / CONSTRAINT_LENGTH)):
    p = int(lines[contraint_index * CONSTRAINT_LENGTH + 4].split(' ')[2])
    q = int(lines[contraint_index * CONSTRAINT_LENGTH + 5].split(' ')[2])
    r = int(lines[contraint_index * CONSTRAINT_LENGTH + 15].split(' ')[2])
    constraints.append((p, q, r))

# idea found on reddit: use z3 lib to solve constraints https://gist.github.com/AdibSurani/c047a0f0d3d9bc294337cb58da16173e#file-aoc2021_day24-py


def solve():
    optimizer = Optimize()
    z = 0  # this is our running z, which has to be zero at the start and end
    v = 0  # this is the value from concatenating our digits
    for contraint_index, (p, q, r) in enumerate(constraints):
        w = Int(f'w{contraint_index}')
        v = v * 10 + w
        optimizer.add(And(w >= 1, w <= 9))  # w is a digit
        z = If(z % 26 + q == w, z/p, 26 * (z/p) + w + r)
    optimizer.add(z == 0)

    optimizer.minimize(v)
    print(optimizer.check())
    print(optimizer.model())
    print(optimizer.model().eval(v))


solve()
