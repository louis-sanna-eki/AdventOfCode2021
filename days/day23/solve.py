from functools import lru_cache
from queue import PriorityQueue
import math

HALLWAY_LENGTH = 11
ROOM_LENGTH = 4

target_x_by_letter = {"A": 2, "B": 4, "C": 6, "D": 8}
target_xs = [target_x for letter, target_x in target_x_by_letter.items()]
hallway_x_by_room_index = {0: 2, 1: 4, 2: 6, 3: 8}

energy_per_step_per_letter = {"A": 1, "B": 10, "C": 100, "D": 1000}

letter_by_room_index = {0: "A", 1: "B", 2: "C", 3: "D"}
room_index_by_letter = {letter: room_index for room_index,
                        letter in letter_by_room_index.items()}


@lru_cache(maxsize=None)
def find_neighbors(hallway: tuple, rooms: tuple) -> list():
    def is_room_free(room_index) -> bool:
        room = rooms[room_index]
        for spot in room:
            if spot == ".":
                continue
            if spot != letter_by_room_index[room_index]:
                return False
        return True

    def is_path_free(start_x, end_x) -> bool:
        if end_x > start_x:
            for hallway_path_x in range(start_x + 1, end_x + 1):
                if hallway[hallway_path_x] != ".":
                    return False
        if end_x < start_x:
            for hallway_path_x in range(end_x, start_x):
                if hallway[hallway_path_x] != ".":
                    return False
        return True

    def is_path_free_to_room(hallway_x) -> bool:
        letter = hallway[hallway_x]
        target_x = target_x_by_letter[letter]
        return is_path_free(hallway_x, target_x)

    def is_path_free_to_hallway(room_index, hallway_x) -> bool:
        room_hallway_x = hallway_x_by_room_index[room_index]
        return is_path_free(room_hallway_x, hallway_x)

    def move_to_room(hallway_x):
        letter = hallway[hallway_x]
        new_hallway = hallway[0:hallway_x] + tuple(".") + hallway[hallway_x+1:]
        final_room_x = target_x_by_letter[letter]
        new_energy = 0
        new_energy += abs(final_room_x - hallway_x) * energy_per_step_per_letter[letter]
        final_room_index = room_index_by_letter[letter]
        new_room = None
        for room_y in range(0, ROOM_LENGTH):
            if rooms[final_room_index][room_y] == ".":
                new_room = rooms[final_room_index][0:room_y] + \
                    tuple(letter) + rooms[final_room_index][room_y+1:]
                new_energy += (ROOM_LENGTH - room_y) * \
                    energy_per_step_per_letter[letter]
                break
        new_rooms = (*rooms[0:final_room_index], new_room,
                     *rooms[final_room_index+1:])
        return new_hallway, new_rooms, new_energy

    def move_to_room_neighbors() -> list:
        result = list()
        for hallway_x, char in enumerate(hallway):
            if char == ".":
                continue
            letter = char
            target_room_index = room_index_by_letter[letter]
            if is_room_free(target_room_index) is False:
                continue
            if is_path_free_to_room(hallway_x) is False:
                continue
            result.append(move_to_room(hallway_x))
        return result

    def find_first_letter_y(room_index) -> int:
        room = rooms[room_index]
        for y in range(ROOM_LENGTH - 1, -1, -1):
            if room[y] != ".":
                return y
        raise Exception('No letter found in this room')

    def move_to_hallway_step(room_index, hallway_x):
        first_letter_y = find_first_letter_y(room_index)
        room = rooms[room_index]
        letter = room[first_letter_y]
        new_hallway = hallway[0:hallway_x] + tuple(letter) + hallway[hallway_x+1:]
        new_room = room[0:first_letter_y] + \
            tuple('.') + room[first_letter_y+1:]
        new_rooms = (*rooms[0:room_index], new_room,
                     *rooms[room_index+1:])
        new_energy = 0
        original_hallway_x = hallway_x_by_room_index[room_index]
        new_energy += abs(original_hallway_x - hallway_x) * \
            energy_per_step_per_letter[letter]
        new_energy += (ROOM_LENGTH - first_letter_y) * \
            energy_per_step_per_letter[letter]
        return new_hallway, new_rooms, new_energy

    def move_to_hallway(room_index) -> list:
        result = list()
        for hallway_x, char in enumerate(hallway):
            if hallway_x in target_xs:  # amphipod cannot stop in front of a room
                continue
            if is_path_free_to_hallway(room_index, hallway_x) is False:
                continue
            result.append(move_to_hallway_step(room_index, hallway_x))
        return result

    def move_to_hallway_neighbors() -> list:
        result = list()
        for room_index, room in enumerate(rooms):
            if is_room_free(room_index):
                continue
            result.extend(move_to_hallway(room_index))
        return result

    result = list()
    result.extend(move_to_room_neighbors())
    result.extend(move_to_hallway_neighbors())
    return result


def is_winning_state(rooms):
    for room_index, room in enumerate(rooms):
        for spot in room:
            if spot != letter_by_room_index[room_index]:
                return False
    return True


visited_by_diagram = dict()
energy_by_diagram = dict()
min_energy = math.inf
diagrams = PriorityQueue()


def visit(hallway, rooms):
    if (hallway, rooms) in visited_by_diagram:
        return
    current_path_energy = energy_by_diagram[(hallway, rooms)]
    neighbors = find_neighbors(hallway, rooms)
    for (n_hallway, n_rooms, n_energy) in neighbors:
        current_lowest_energy = energy_by_diagram[(n_hallway, n_rooms)] if (
            n_hallway, n_rooms) in energy_by_diagram else math.inf
        n_current_path_energy = current_path_energy + n_energy
        if n_current_path_energy <= current_lowest_energy:
            energy_by_diagram[(n_hallway, n_rooms)] = n_current_path_energy
            n_tuple = tuple((n_hallway, n_rooms))
            diagrams.put(tuple((n_current_path_energy, n_tuple)))
    visited_by_diagram[(hallway, rooms)] = True


def part1():
    starting_hallway = tuple(".") * HALLWAY_LENGTH
    # starting_rooms = (("A", "B"), ("D", "C"), ("C", "B"), ("A", "D"))  # sample
    # starting_rooms = (("D", "D"), ("A", "B"), ("B", "C"), ("A", "C")) # part1
    starting_rooms = (("D", "D", "D", "D"), ("A", "B", "C", "B"),
                      ("B", "A", "B", "C"), ("A", "C", "A", "C"))
    energy_by_diagram[(starting_hallway, starting_rooms)] = 0
    visit(starting_hallway, starting_rooms)
    while not diagrams.empty():
        priority, (hallway, rooms) = diagrams.get()
        visit(hallway, rooms)
    print(energy_by_diagram[(starting_hallway,
          (("A", "A", "A", "A"), ("B", "B", "B", "B"), ("C", "C", "C", "C"), ("D", "D", "D", "D")))])


part1()
