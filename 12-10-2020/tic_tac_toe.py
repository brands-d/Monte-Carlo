from numpy.random import randint, permutation
import numpy as np


def tic_tac_toe(num_plays=1e2):

    one_won = 0
    minus_one_won = 0
    for _ in range(num_plays):
        play_field = np.zeros((3, 3))
        turn = 1
        turn_order = permutation(range(9))
        for i in turn_order:
            if turn == 1:
                play_field[int(i / 3)][i % 3] = 1
                turn = -1
            else:
                play_field[int(i / 3)][i % 3] = -1
                turn = 1

            if is_win(play_field) == 1:
                one_won += 1
                break

            if is_win(play_field) == -1:
                minus_one_won += 1
                break

    return one_won, minus_one_won, num_plays - (one_won + minus_one_won)


def is_win(play_field):
    for i in range(3):

        if (play_field[:, i] == 1).all():
            return 1
        elif (play_field[:, i] == -1).all():
            return -1

        if (play_field[i, :] == 1).all():
            return 1
        elif (play_field[i, :] == -1).all():
            return -1

    if (play_field[[0, 1, 2], [0, 1, 2]] == 1).all():
        return 1
    elif (play_field[[0, 1, 2], [0, 1, 2]] == -1).all():
        return -1

    if (play_field[[2, 1, 0], [0, 1, 2]] == 1).all():
        return 1
    elif (play_field[[2, 1, 0], [0, 1, 2]] == -1).all():
        return -1

    return 0


num_plays = 100000
result = np.array(tic_tac_toe(num_plays))

first_win = [1] * result[0] + [0] * (result[1] + result[2])

print(str(result[0] / num_plays) + ' +- ' +
      str(np.sqrt(np.var(first_win) / np.sqrt(num_plays))))
