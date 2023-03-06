from typing import Callable

import scipy
import numpy as np
import matplotlib.pyplot as plt
import seaborn


def generate(path: str, num: int, dist_rvs: Callable, *args) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(map(str, dist_rvs(*args, size=num))))


def read(path: str) -> np.ndarray:
    with open(path, 'r', encoding='utf-8') as f:
        return np.array(f.read().split('\n'), dtype=float)


def main():
    M = 6500
    K = 10
    _lambda = 1.5

    # 2 - 3
    # generate('uni_10.txt', M, scipy.stats.uniform.rvs)
    # generate('pois_10.txt', M, scipy.stats.poisson.rvs, _lambda)

    uni = read('uni_10.txt')
    pois = read('pois_10.txt')

    # 4.1
    print(uni[:K])
    print(pois[:K])
    print()

    # 4.2 - 4.3
    print(f'Uniform distribution:\n Max: {uni.max()}\n Min: {uni.min()}\n Mean: {uni.mean()}')
    print(f'Poisson distribution:\n Max: {pois.max()}\n Min: {pois.min()}\n Mean: {pois.mean()}')
    print()
    # 4.4
    L = [32, 316, 1000, 3162, M]

    x_log = np.log10(L)
    y_mean = [uni[:l].mean() for l in L]

    plt.figure()
    plt.plot(x_log, y_mean)
    plt.title('Dependence of mean on size')
    plt.xlabel('log10(L)')
    plt.ylabel('Mean')
    plt.show()

    # 4.5
    uni_theor_std = scipy.stats.uniform.std(_lambda)
    print(f'Uni std: theor: {uni_theor_std} emp: {uni.std()} diff: {uni_theor_std - uni.std()}')
    print(f'Pois std: theor: {scipy.stats.poisson.std(_lambda)} emp: {pois.std()}')
    print()

    seaborn.set()
    plt.figure()
    seaborn.histplot(data=[uni, np.linspace(uni.min(), uni.max(), M)], stat='probability')
    plt.show()

    plt.figure()
    a = []
    for i in [[el] * int(M * scipy.stats.poisson.pmf(el, _lambda)) for el in range(0, int(pois.max()))]:
        a.extend(i)
    seaborn.histplot(data=[pois, a], stat='probability')
    plt.show()

    # 4.6
    plt.figure()
    seaborn.ecdfplot(data=[uni])
    x = np.linspace(0, 1, 100)
    plt.plot(x, scipy.stats.uniform.cdf(x))
    plt.legend(['empirical', 'theoretical'])
    plt.show()


if __name__ == "__main__":
    main()
