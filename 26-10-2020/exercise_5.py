from numpy.random import rand
import numpy as np
import matplotlib.pyplot as plt
import time


def marsaglia(dim, L, num):

    lattice = np.zeros([L] * dim, dtype=bool)
    untagged = [L**dim]

    for _ in range(1, num):
        x = np.floor(rand(dim) * L).astype(np.int32)
        lattice[tuple(x)] = True
        untagged.append(L**dim -np.count_nonzero(lattice))
    return untagged


dim, L, num = 2, 200, 500000

start_time = time.time()
untagged = marsaglia(dim, L, num)
print("--- %s seconds ---" % (time.time() - start_time))

fig, ax = plt.subplots()

ax.plot(list(range(num)), untagged)

ax.grid()
ax.set(xlabel='# of random points', ylabel='# untagged points')
plt.show()
