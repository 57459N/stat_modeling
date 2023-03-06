import matplotlib.pyplot as plt
from numpy import linspace
from lab1_2 import solve


def main():
    steps = 500
    _x = linspace(-5, 5, num=steps, endpoint=True)
    _y = solve(_x)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(_x, _y)

    ax.set_title('x^3 + 2x^2 + 2 polynomial')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.grid(visible=True, color='orange', linestyle='-', linewidth=0.5)

    ax.set_xticks(linspace(-5, 5, 10))
    ax.set_yticks(linspace(_y.min(), _y.max(), 10))

    plt.show()


if __name__ == "__main__":
    main()
