from copy import deepcopy

HALLWAY_LENGTH = 11
ROOM_LENGTH = 2

x_by_letter = {"A": 2, "B": 3, "C": 4, "D": 5}


letter_by_room_index = {0: "A", 1: "B", 2: "C", 3: "D"}
room_index_by_letter = {letter: room_index for room_index,
                        letter in letter_by_room_index.items()}


def find_neighbors(hallway, rooms) -> list():

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
        final_room_index = room_index_by_letter[letter]
        for hallway_x in range(hallway_x + 1, final_room_index, 1 if final_room_index > hallway_x else -1):
            if hallway[hallway_x] != ".":
                return False
        return True

    def move_to_room(hallway_x):
        letter = hallway[hallway_x]
        new_hallway = hallway.copy()
        new_hallway[hallway_x] = "."
        new_rooms = deepcopy(rooms)
        final_room_x = x_by_letter[letter]
        new_energy = 0
        new_energy += abs(final_room_x - hallway_x)
        final_room_index = room_index_by_letter[letter]
        for room_y in range(0, ROOM_LENGTH):
            if new_rooms[final_room_index][room_y] == ".":
                new_rooms[final_room_index][room_y] = letter
                new_energy += ROOM_LENGTH - room_y
                break
        return new_hallway, new_rooms, new_energy

    result = list()
    for hallway_x, char in enumerate(hallway):
        if char == ".":
            continue
        letter = char
        final_room_index = room_index_by_letter[letter]
        if is_room_free(final_room_index) is False:
            continue
        if is_path_free(hallway_x) is False:
            continue
        result.append(move_to_room(hallway_x))
    return result