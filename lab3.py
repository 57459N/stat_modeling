import math
import random

import scipy

from lab2 import generate, read
import matplotlib.pyplot as plt
import numpy as np
import seaborn


def my_rvs(size: int | None = None) -> float | np.ndarray[float]:
    if size is None:
        return random.random() * 10
    else:
        return np.array([random.random() * 10 for _ in range(size)], dtype=float)


def main():
    # generate('lab3_values.txt', 3000, my_rvs)
    values = read('lab3_values.txt')

    seaborn.ecdfplot(values)
    plt.show()

    print(
        f'Mean: calculated: {values.sum() / len(values)} \t {values.mean()=} \t theoretical pdf: {0.1/2 * 10 ** 2 = }')

    margin = (2.88675 / math.sqrt(len(values)) * 1.96)
    print(margin)
    print(scipy.stats.uniform(0, 10).interval(0.95))
    print(f'Confidential interval: [{values.mean() - margin} : {values.mean() + margin}]')

    variance = 1. / (len(values) - 1) * (sum(map(lambda x: x ** 2, values)) - values.sum() ** 2 / len(values))
    print(f'Variance: calculated: {variance} \t {values.var()=} \t theoretical pdf: 8.33333')

    seaborn.histplot(data=[values, np.linspace(0, 10, len(values))], stat='probability')
    plt.show()


if __name__ == "__main__":
    main()
