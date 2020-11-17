import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def P(x):
    return np.sqrt(2 / np.pi)*(x**2 * np.exp(-x**2 / 2))


def reject(p):

    if np.random.uniform() < p:
        return False

    else:
        return True

raw = P(np.random.uniform(size=100000))
filtered = [i for i in raw if reject(i)]

plt.hist(filtered)
plt.show()