def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for game_round in range(len(game)):
        if game[game_round] == '/':
            result += 10 - last
        else:
            result += get_value(game[game_round])
        if frame < 10  and get_value(game[game_round]) == 10:
            if game[game_round] == '/':
                result += get_value(game[game_round+1])
            elif game[game_round] in 'Xx':
                result += get_value(game[game_round+1])
                if game[game_round+2] == '/':
                    result += 10 - get_value(game[game_round+1])
                else:
                    result += get_value(game[game_round+2])
        last = get_value(game[game_round])
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if game[game_round] in 'Xx':
            in_first_half = True
            frame += 1
    return result

def get_value(char):
    return int(char) if char in "123456789" else 10 if char.upper() in "X/" else 0 if char == "-" else ValueError