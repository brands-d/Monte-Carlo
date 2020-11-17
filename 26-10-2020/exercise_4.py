from numpy.random import rand
import numpy as np
import time


def single_rand_test(k, sample_size, num_samples):

    x_should = 1 / (k + 1)

    x_mean = []
    for _ in range(num_samples):
        x_k = rand(sample_size)**k

        x_mean.append(np.mean(x_k))

    x_is = np.mean(x_mean)
    std = np.std(x_mean) / np.sqrt(num_samples)

    return [x_is, std], x_should


def double_rand_test(k, k_prime, sample_size, num_samples):

    C_should = 1 / ((k + 1) * (k_prime + 1))

    C_mean = []
    for _ in range(num_samples):
        x_k = rand(sample_size)**k
        x_k_prime = rand(sample_size)**k_prime
        product = x_k * x_k_prime

        C_mean.append(np.mean(product))

    C_is = np.mean(C_mean)
    std = np.std(C_mean) / np.sqrt(num_samples)

    return [C_is, std], C_should


print('--- Single Variable Test ---')
start_time = time.time()

k, sample_size, num_samples = 5, 10000, 1000
x_is, x_should = single_rand_test(k, sample_size, num_samples)

print('{0:.7f} +- {1:.7f} ({2:.7f})'.format(*x_is, x_should))
print('--- {0:.3f} seconds ---'.format(time.time() - start_time))


print()
print('--- Double Variable Test ---')
start_time = time.time()

k, sample_size, num_samples = 5, 10000, 1000
C_is, C_should = double_rand_test(k, k, sample_size, num_samples)

print('{0:.8f} +- {1:.8f} ({2:.8f})'.format(*C_is, C_should))
print('--- {0:.3f} seconds ---'.format(time.time() - start_time))
