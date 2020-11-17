import numpy as np
from numpy.random import randint
import time


def euclidean_distance(x):

    return np.sqrt(np.sum(x**2, axis=1))


def manhatten_distance(x):

    return np.sum(np.absolute(x), axis=1)


def random_walk(steps, backtrack_allowed=False):

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    last_move = [0, 0]
    pos = [np.array([0, 0])]

    for _ in range(steps):

        if not backtrack_allowed:
            prohibted_move = list(np.array(last_move) * -1)
            possible_moves = [
                move for move in directions if move != prohibted_move]
            last_move = possible_moves[randint(0, len(possible_moves))]

        else:
            last_move = directions[randint(0, len(directions))]

        pos.append(pos[-1] + last_move)

    pos = np.array(pos)
    distance_euclidean = euclidean_distance(pos)
    distance_manhatten = manhatten_distance(pos)

    return distance_euclidean, distance_manhatten


def random_walk_sampling(samples, steps, **kwargs):

    de_means = []
    de_maxs = []
    dm_means = []
    dm_maxs = []

    for _ in range(samples):
        de, dm = random_walk(steps, **kwargs)

        de_means.append(np.mean(de))
        de_maxs.append(np.max(de))
        dm_means.append(np.mean(dm))
        dm_maxs.append(np.max(dm))

    de_mean = [np.mean(de_means), np.std(de_means) / np.sqrt(steps)]
    de_max = [np.mean(de_maxs), np.std(de_maxs) / np.sqrt(steps)]
    dm_mean = [np.mean(dm_means), np.std(dm_means) / np.sqrt(steps)]
    dm_max = [np.mean(dm_maxs), np.std(dm_maxs) / np.sqrt(steps)]

    return de_mean, de_max, dm_mean, dm_max


start_time = time.time()

sample_size, steps = 100, 5000

print('--- {0:.0f} Random Walks with {1:.0f} steps each ---'.format(sample_size, steps))

de_mean, de_max, dm_mean, dm_max = random_walk_sampling(
    sample_size, steps, backtrack_allowed=True)

print('Euclidean Distance: Avg. = {0:.2f} +- {1:.2f}; Max = {2:.2f} +- {3:.2f}'.format(*de_mean, *de_max))
print('Manhatten Distance: Avg. = {0:.2f} +- {1:.2f}; Max = {2:.2f} +- {3:.2f}'.format(*dm_mean, *dm_max))
print('--- {0:.3f} seconds ---'.format(time.time() - start_time))
