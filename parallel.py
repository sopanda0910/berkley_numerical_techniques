import multiprocessing as mp
import time
import numpy as np

import matplotlib.pyplot as plt

def random_square(seed):
    np.random.seed(seed)
    random_num = np.random.randint(0, 10)
    return random_num**2

def serial(n):
    t0 = time.time()
    results = []
    for i in range(n): 
        results.append(random_square(i))
    t1 = time.time()
    return (t1-t0)

def parallel(n):
    t0 = time.time()
    n_cpu = mp.cpu_count()
    pool = mp.Pool(processes=n_cpu)
    results = [pool.map(random_square, range(n))]
    t1 = time.time()
    return (t1 - t0)

# This is critical for parallel processing since if not there, 
# then each child worker will instantiate even more workers
# and there would be an infinite loop
if __name__ == '__main__':
    n_run = np.logspace(1, 7, 7)

    t_serial = [serial(int(n)) for n in n_run]
    t_parallel = [parallel(int(n)) for n in n_run]

    plt.figure(figsize = (10, 6))
    plt.plot(n_run, t_serial, '-o', label = 'serial')
    plt.plot(n_run, t_parallel, '-o', label = 'parallel')
    plt.loglog()
    plt.legend()
    plt.ylabel('Execution time (s)')
    plt.xlabel('Number of random points')
    plt.show()
