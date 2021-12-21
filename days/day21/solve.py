

def generate_deterministic_roll():
    deterministic_roll_count = 0

    def roll():
        nonlocal deterministic_roll_count
        roll = (deterministic_roll_count % 100) + 1
        deterministic_roll_count += 1
        return roll

    def roll_count():
        return deterministic_roll_count
    return roll, roll_count


roll, roll_count = generate_deterministic_roll()


def move(start, steps):
    return ((start + steps - 1) % 10) + 1


def play(player):  # beware side-effect
    rolls = roll() + roll() + roll()
    player["position"] = move(player["position"], rolls)
    player["score"] += player["position"]


player1 = dict({"position": 6, "score": 0})
player2 = dict({"position": 9, "score": 0})


def part_1():
    while (True):
        play(player1)
        print("player1['score']", player1["score"])
        print("player1['position']", player1["position"])
        if (player1["score"] >= 1000):
            break
        play(player2)
        if (player2["score"] >= 1000):
            break
    print("roll_count", roll_count())
    print("player1['score']", player1["score"])
    print("player2['score']", player2["score"])


part_1()
