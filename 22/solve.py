def solve_part_1(data):
    parts = data.split("\n\n")
    player_1_cards = [int(card) for card in parts[0].split("\n")[1:]]
    player_2_cards = [int(card) for card in parts[1].split("\n")[1:]]

    round_number = 1
    while not len(player_1_cards) == 0 and not len(player_2_cards) == 0:
        top_1 = player_1_cards.pop(0)
        top_2 = player_2_cards.pop(0)
        if top_1 > top_2:
            player_1_cards.append(top_1)
            player_1_cards.append(top_2)
        else:
            player_2_cards.append(top_2)
            player_2_cards.append(top_1)
        round_number += 1
    score = 0
    winner_cards = player_1_cards
    if len(player_1_cards) == 0:
        winner_cards = player_2_cards
    winner_cards.reverse()
    for i, card in enumerate(winner_cards):
        score += (i + 1) * card
    return score


def game_to_str(p1, p2):
    p1s = str(p1)
    p2s = str(p2)
    return p1s + p2s


def copy_cards(cards, n):
    new_cards = []
    for i in range(n):
        new_cards.append(cards[i])
    return new_cards


game_to_played_rounds = {}
global_game_count = 1


def play_recursive(player_1_cards, player_2_cards, game_number):
    global global_game_count
    global game_to_played_rounds

    round_number = 1
    winner = "p1"
    while not len(player_1_cards) == 0 and not len(player_2_cards) == 0:
        played_rounds_this_game = game_to_played_rounds.get(game_number, set())
        game_str = game_to_str(player_1_cards, player_2_cards)
        if game_str in played_rounds_this_game:
            return "p1"

        played_rounds_this_game.add(game_str)
        game_to_played_rounds[game_number] = played_rounds_this_game

        top_1 = player_1_cards.pop(0)
        top_2 = player_2_cards.pop(0)
        if len(player_1_cards) >= top_1 and len(player_2_cards) >= top_2:
            global_game_count += 1
            winner = play_recursive(copy_cards(player_1_cards, top_1), copy_cards(player_2_cards, top_2), global_game_count)
        else:
            if top_1 > top_2:
                winner = "p1"
            else:
                winner = "p2"
        if winner == "p1":
            player_1_cards.append(top_1)
            player_1_cards.append(top_2)
        else:
            player_2_cards.append(top_2)
            player_2_cards.append(top_1)
        round_number += 1
    if game_number == 1:
        score = 0
        winner_cards = player_1_cards
        if len(player_1_cards) == 0:
            winner_cards = player_2_cards
        winner_cards.reverse()
        for i, card in enumerate(winner_cards):
            score += (i + 1) * card
        return score
    return winner


def solve_part_2(data):
    parts = data.split("\n\n")
    player_1_cards = [int(card) for card in parts[0].split("\n")[1:]]
    player_2_cards = [int(card) for card in parts[1].split("\n")[1:]]
    return play_recursive(player_1_cards, player_2_cards, 1)


def solve():
    # data = open('easy.txt', 'r').read()
    data = open('input.txt', 'r').read()
    print("Part 1:", solve_part_1(data))
    print("Part 2:", solve_part_2(data))


solve()
