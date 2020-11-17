# Python Imports
import time

# Third Party Imports
import numpy as np
import matplotlib.pyplot as plt

# Own Imports
from pi import monte_carlo


# Main Program
print('------------- PI Calculation with Monte Carlo -------------')
dim, num_points = 10, 1e5
pi, std = monte_carlo(dim=dim, num_points=num_points)
print('Pi:\t\t%f\nStd:\t\t%f' % (pi, std))

