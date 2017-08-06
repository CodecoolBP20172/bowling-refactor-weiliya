def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        result += handle_spare(game, i)

        if is_not_last_frame(frame):
            if is_spare(game[i]):
                result += get_next_value_for_spare(game, i)
            elif is_strike(game[i]):
                result += get_next_value_for_strike(game, i)

        if not in_first_half:
            frame += 1

        in_first_half = not in_first_half

        if is_strike(game[i]):
            in_first_half = True
            frame += 1
    return result


def handle_spare(game, i):
    result = 0
    if is_spare(game[i]):
        result += 10 - get_value(game[i - 1])
    else:
        result += get_value(game[i])
    return result


def get_next_value_for_strike(game, i):
    i = i+1
    result = get_value(game[i])
    result += handle_spare(game, i+1)

    return result


def get_next_value_for_spare(game, i):
    return get_value(game[i + 1])


def is_not_last_frame(frame):
    return frame < 10


def get_value(char):
    if is_simple_point(char):
        return int(char)
    elif is_strike(char) or is_spare(char):
        return 10
    elif is_miss(char):
        return 0
    else:
        raise ValueError("Invalid value: " + char)


def is_strike(char):
    return char == 'X' or char == 'x'


def is_spare(char):
    return char == '/'


def is_miss(char):
    return char == '-'


def is_simple_point(char):
    return char == '1' or char == '2' or char == '3' \
           or char == '4' or char == '5' or char == '6' \
           or char == '7' or char == '8' or char == '9'