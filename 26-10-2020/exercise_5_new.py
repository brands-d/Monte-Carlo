import numpy as np
from LFSR import *
import matplotlib.pyplot as plt

L = 10000
num_untagged = [L**2]
n = 2000000
lattice = np.zeros((L, L), dtype=np.bool)

for _ in range(n):
    x = int(next(LCGgen2) * L)
    y = int(next(LCGgen2) * L)

    if lattice[x][y] == False:
        lattice[x][y] = True
        num_untagged.append(num_untagged[-1] - 1)

    else:
        num_untagged.append(num_untagged[-1])


fig, ax = plt.subplots()

ax.plot(list(range(n+1)), num_untagged)

ax.grid()
ax.set(xlabel='# of random points', ylabel='# untagged points', title='{}x{} ={} Lattice'.format(L,L,L**2))

plt.imshow(lattice)
plt.show()
