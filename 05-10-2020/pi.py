# Python Imports
import numpy as np

# Third Party Imports
from numpy.random import rand
from scipy.special import gamma


def monte_carlo(dim=2, num_points=10e6, memory_boundary=2000, verbose=False):

    def _raw_count(dim, num_points, radius=1):

        points = rand(int(dim), int(num_points))
        radii = np.sum(points**2, axis=0)
        count = len(radii[radii <= radius])

        return count

    single_point_memory_cost = rand(1).itemsize
    memory_cost = dim * num_points * single_point_memory_cost

    if memory_cost > memory_boundary * 1000:
        if verbose:
            print('Memory cost of a %ix%i array (%i MB) larger than available memory (%i MB).' % (
                dim, num_points, memory_cost / 1000, memory_boundary))

        loop_num_points = int(memory_boundary *
                              1000 / (dim * single_point_memory_cost))
        loop_count = int(num_points / loop_num_points)
        remainder = num_points % loop_num_points

        if remainder == 0:
            if verbose:
                print('Counting process gets split into %i loops of %i points.' % (
                    loop_count, loop_num_points))

            count = 0

        else:
            if verbose:
                print('Counting process gets split into %i loops of %i points plus a loop with the remaining %i points.' % (
                    loop_count, loop_num_points, remainder))

            count = _raw_count(dim, remainder)

        for i in range(loop_count):
            count += _raw_count(dim, loop_num_points)

    else:
        count = _raw_count(dim, num_points)

    pi = (2**dim * gamma(dim / 2 + 1) * count / num_points)**(2 / dim)
    std = 1 / np.sqrt(num_points)

    return pi, std
