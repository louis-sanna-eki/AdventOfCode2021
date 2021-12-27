from functools import lru_cache

HALLWAY_LENGTH = 11
ROOM_LENGTH = 2

target_x_by_letter = {"A": 2, "B": 4, "C": 6, "D": 8}

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

    def is_path_free(hallway_x):
        letter = hallway[hallway_x]
        target_x = target_x_by_letter[letter]
        if target_x > hallway_x:
            for hallway_path_x in range(hallway_x + 1, target_x + 1):
                if hallway[hallway_path_x] != ".":
                    return False
        if target_x < hallway_x:
            for hallway_path_x in range(target_x, hallway_x):
                if hallway[hallway_path_x] != ".":
                    return False
        return True

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

    result = list()
    for hallway_x, char in enumerate(hallway):
        if char == ".":
            continue
        letter = char
        target_room_index = room_index_by_letter[letter]
        if is_room_free(target_room_index) is False:
            continue
        if is_path_free(hallway_x) is False:
            continue
        result.append(move_to_room(hallway_x))
    return result
