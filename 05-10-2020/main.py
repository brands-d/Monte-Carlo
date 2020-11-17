# Python Imports
import time

# Third Party Imports
import numpy as np
import matplotlib.pyplot as plt

# Own Imports
from pi import monte_carlo


def pretty_print(func, dim, num_points, *args, **kwargs):

    start_time = time.time()
    pi, std = func(dim, num_points, verbose=True)
    end_time = time.time()

    print('Dim:\t\t%i' % dim)
    print('Num. Points:\t%i' % num_points)
    print('Pi:\t\t%f (%f)' % (pi, np.pi))
    print('Std:\t\t%f' % std)
    print('Abs. Diff:\t%f' % (pi - np.pi))
    print('Time:\t\t%f s' % (end_time - start_time))


# Main Program
print('------------- PI Calculation with Monte Carlo -------------')
dim, num_points = 10, 1e2
pretty_print(monte_carlo, dim=dim, num_points=num_points)

fig, ax = plt.subplots(1)

for dim in [2, 4, 8, 10]:

    points = np.logspace(2, 6, num=50)
    results_MC = []

    for num_points in points:
        results_MC.append(monte_carlo(dim, int(num_points)))

    ax.plot(points, np.array(results_MC)[:, 0], label='dim: %i' % dim)
    
ax.legend()
ax.grid()
ax.set(xlabel='# points', ylabel='pi')
plt.show()
