import time
import numpy as np
import functools


def profile(fn):
    no_iterations = 8

    def wrap(*args, **kwargs):
        time_array = np.empty(no_iterations)
        return_value = None
        for idx in range(no_iterations):
            start = time.time()
            return_value = fn(*args, **kwargs)
            end = time.time()
            time_array[idx] = end-start

        print "Function {}: mean elapsed {}s".format(
            fn.__name__, np.mean(time_array))
        print "Function {}: min elapsed {}s".format(
            fn.__name__, np.min(time_array))
        print "Function {}: max elapsed {}s".format(
            fn.__name__, np.max(time_array))

        return return_value

    return wrap


@profile
def matrix_multiply_fast(mat_1, mat_2):
    return np.dot(mat_1, mat_2)


@profile
def matrix_multiply_slow(mat_1, mat_2):
    mat = np.zeros((mat_1.shape[0], mat_2.shape[1]))
    for i in range(mat_1.shape[0]):
        for j in range(mat_2.shape[1]):
            mat[i, j] = np.dot(mat_1[i, :], mat_2[:, j])
    return mat


@profile
def generate_data():
    mat_1 = np.random.random((100, 1000))
    mat_2 = np.random.random((1000, 5000))
    return mat_1, mat_2


def main():
    m1, m2 = generate_data()
    mat_1 = matrix_multiply_fast(m1, m2)
    mat_2 = matrix_multiply_slow(m1, m2)
    # assert all matrix elements are numerically equivalent
    np.testing.assert_allclose(mat_1, mat_2)
    return mat_1


if __name__ == '__main__':
    main()
