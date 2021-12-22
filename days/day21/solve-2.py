import sys
sys.setrecursionlimit(10000)


def move(start, steps):
    return ((start + steps - 1) % 10) + 1


def play(player, steps):  # beware side-effect
    player["position"] = move(player["position"], steps)
    player["score"] += player["position"]


player1 = dict({"position": 6, "score": 0})
player2 = dict({"position": 9, "score": 0})


def hash_players(player1, player2):
    return f'{player1["position"]}-{player1["score"]}-{player2["position"]}-{player2["score"]}'


def build_count_winning():

    cache = dict()

    def count_winning(player1, player2):
        hash = hash_players(player1, player2)
        if hash in cache:
            return cache[hash]
        if player1["score"] >= 21:
            cache[hash] = 1, 0
            return 1, 0

        if player2["score"] >= 21:
            cache[hash] = 0, 1
            return 0, 1

        player_1_wins = 0
        player_2_wins = 0

        for dice_1 in range(1, 4):
            for dice_2 in range(1, 4):
                for dice_3 in range(1, 4):
                    new_player1 = player1.copy()
                    new_player2 = player2.copy()
                    steps = dice_1 + dice_2 + dice_3
                    play(new_player1, steps)
                    # player 2 becomes player 1 since it's its turn to play
                    new_player2_wins, new_player1_wins = count_winning(
                        new_player2, new_player1)
                    player_1_wins += new_player1_wins
                    player_2_wins += new_player2_wins

        cache[hash] = player_1_wins, player_2_wins
        return player_1_wins, player_2_wins

    return count_winning


def part2():
    count_winning = build_count_winning()
    player_1_wins, player_2_wins = count_winning(player1, player2)
    print(player_1_wins, player_2_wins)
    print("player 1 is bigger: ", player_1_wins >= player_2_wins)


part2()
