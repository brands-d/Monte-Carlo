import numpy as np
from LFSR import *


def mean(numbers):

    mean = np.mean(numbers)
    std = np.std(numbers) / np.sqrt(len(numbers))

    return mean, std

k = 3
n = 10000
should = 1/(k+1)
numbers = [next(gen) for _ in range(n)]
mean = mean(np.array(numbers)**k)
print('Error: ', str(abs(mean[0]-should)/mean[1]))