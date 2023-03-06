import numpy as np
import scipy
from pprint import pprint


def main():
    a = np.array([[5, -1],
                  [1, -1]],
                 dtype=float)
    b = np.array([[14],
                  [6]],
                 dtype=float)

    pprint(scipy.linalg.solve(a, b))


if __name__ == "__main__":
    main()
