"""
This example shall model mapping a computationally expensive task (
modeled by an idle) matrix product with different arguments.
"""

import multiprocessing
import os
import numpy as np
import warnings

from decorator_stuff.profile_decorator import profile


def translate_exception_decorator(fn):
    # this is not pickleable unfortunately and can't be used with
    # multiprocessing
    def wrap(*args, **kwargs):
        try:
            res = fn(*args, **kwargs)
        except Exception as exc:
            warnings.warn("Caught Exception of type {}: {}".format(
                type(exc), exc))
            res = None

        return res

    return wrap


def translate_exception_fn(*args, **kwargs):
    try:
        res = worker_main(*args, **kwargs)
    except Exception as exc:
        res = exc

    return res


def worker_main(dt):
    if dt == 3:
        raise ValueError(
            "For some reason, this computation throws an exception.")
    print os.getpid(), "working"
    print "dt = {}".format(dt)
    # a somewhat heavy computation to get the CPU to compute something
    a = np.random.random((1000, 1000))
    _ = dt*np.dot(a, a)
    print os.getpid(), "finished computation"


# this is a somewhat dirty workaround ...
worker_main_safe = translate_exception_fn


@profile
def main():
    dts = np.arange(15)
    # start a pool with 2 processes
    the_pool = multiprocessing.Pool(2)
    # work 15 jobs on the 2 processes
    the_pool.map(worker_main_safe, dts)


if __name__ == '__main__':
    main()

