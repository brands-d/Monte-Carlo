# Python Imports
import numpy as np

# Third Party Imports
from numpy.random import rand
from scipy.special import gamma


def monte_carlo(dim=2, num_points=10e6):

    points = rand(int(dim), int(num_points))
    radii = np.sqrt(np.sum(points**2, axis=0))
    std = np.sqrt(np.sum((radii - np.mean(radii)) **
                         2, axis=0) / (np.sqrt(num_points) * (num_points - 1)))
    count = len(radii[radii <= 1])
    pi = (2**dim * gamma(dim / 2 + 1) * count / num_points)**(2 / dim)

    return pi, std
