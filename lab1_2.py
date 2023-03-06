import numpy as np
from numpy import ndarray


def solve(x: float | ndarray):
    a = 1
    b = 2
    c = 2

    return a * x ** 3 + b * x ** 2 + c


def main():
    print(solve(3))

    print(solve(np.array([[1, 2]])))

    print(solve(np.array([[1],
                          [2]])))


if __name__ == "__main__":
    main()
