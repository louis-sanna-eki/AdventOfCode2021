file = open('days/day11/input.txt', 'r')
lines = file.read().splitlines()
file.close()

octopuses = [list(map(int, line)) for line in lines]

NUMBER_OF_STEPS = 100


def simulate_step():
    flashes = [[False] * len(line) for line in lines]

    def set_flashed_to_zero():
        result = 0
        for i in range(0, len(octopuses)):
            for j in range(0, len(octopuses[i])):
                if flashes[i][j] is True:
                    octopuses[i][j] = 0
                    result += 1
        return result

    def add_energy_to_octopuses():
        for i in range(0, len(octopuses)):
            for j in range(0, len(octopuses[i])):
                add_energy(i, j)

    def add_energy(i, j):
        if is_in_array(i, j) is False:
            return
        if flashes[i][j]:
            return
        octopuses[i][j] += 1
        if octopuses[i][j] > 9:
            flash(i, j)

    def flash(i, j):
        if is_in_array(i, j) is False:
            return
        if flashes[i][j]:
            return
        flashes[i][j] = True
        add_energy(i+1, j)
        add_energy(i-1, j)
        add_energy(i, j+1)
        add_energy(i, j-1)
        add_energy(i-1, j-1)
        add_energy(i+1, j+1)
        add_energy(i+1, j-1)
        add_energy(i-1, j+1)

    def is_in_array(i, j):
        if i < 0:
            return False
        if j < 0:
            return False
        if i >= len(octopuses):
            return False
        if j >= len(octopuses[i]):
            return False
        return True

    add_energy_to_octopuses()
    flash_count = set_flashed_to_zero()
    return flash_count


result = 0
for step in range(1, NUMBER_OF_STEPS + 1):
    result += simulate_step()

print(result)
