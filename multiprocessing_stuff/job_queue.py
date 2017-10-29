"""
This example shall model mapping a computationally expensive task (
modeled by an idle) matrix product with different arguments.
"""

import multiprocessing
import os
import numpy as np


def worker_main(dt):
    print os.getpid(), "working"
    print "dt = {}".format(dt)
    a = np.random.random((7000, 7000))
    _ = dt*np.dot(a, a)
    print os.getpid(), "finished computation"


def main():
    dts = np.arange(15)
    # start a pool with 2 processes
    the_pool = multiprocessing.Pool(2)
    # work 15 jobs on the 2 processes
    the_pool.map(worker_main, dts)


if __name__ == '__main__':
    main()

