import os
import numpy as np
import concurrent.futures

from decorator_stuff.profile_decorator import profile


def worker_main(dt):
    if dt == 3:
        raise ValueError(
            "For some reason, this computation throws an exception.")
    print os.getpid(), "working"
    print "dt = {}".format(dt)
    a = np.random.random((1000, 1000))
    # a somewhat heavy computation to get the CPU to compute something
    _ = dt*np.dot(a, a)
    print os.getpid(), "finished computation"


@profile
def main():
    dts = np.arange(15)
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        # we create a dictionary with the futures as keys and the arguments as
        # values
        computed_work = {executor.submit(worker_main, dt): dt for dt in
                         dts}
        for future in concurrent.futures.as_completed(computed_work):
            dt = computed_work[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%d generated an exception: %s' % (dt, exc))
            else:
                print('%d computed successfully' % dt)
                print('Data: {}'.format(data))


if __name__ == '__main__':
    main()
