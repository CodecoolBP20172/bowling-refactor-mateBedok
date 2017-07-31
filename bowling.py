def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for game_roll in range(len(game)):
        if game[game_roll] == '/':
            result += 10 - last_point
        else:
            result += get_value(game[game_roll])
        if frame < 10  and get_value(game[game_roll]) == 10:
            result = is_spare_or_strike(game, game_roll, result)
        frame, in_first_half = frame_check(frame, game, game_roll, in_first_half)
        last_point = get_value(game[game_roll])
    return result


def is_spare_or_strike(game, game_roll, result):
    if game[game_roll] == '/':
        result += get_value(game[game_roll+1])
    elif game[game_roll] in 'Xx':
        result += get_value(game[game_roll+1])
        if game[game_roll+2] == '/':
            result += 10 - get_value(game[game_roll+1])
        else:
            result += get_value(game[game_roll+2])
    return result


def frame_check(frame, game, game_roll, in_first_half):
    if not in_first_half:
        frame += 1
    if in_first_half == True:
        in_first_half = False
    else:
        in_first_half = True
    if game[game_roll] in 'Xx':
        in_first_half = True
        frame += 1
    return frame, in_first_half


def get_value(char):
    return int(char) if char in "123456789" else 10 if char.upper() in "X/" else 0 if char == "-" else ValueError
