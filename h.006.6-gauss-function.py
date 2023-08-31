import math
import matplotlib.pyplot as plt
from numpy import arange


def get_gauss():
    x = arange(-10.0, 10.0, 0.1)
    y = []

    for value in x:
        y.append(gauss_function(value))

    plt.plot(x, y)
    plt.show()


def gauss_function(value):
    return (1 / math.sqrt(2 * math.pi)) * (math.e ** (-0.5 * (value ** 2)))


get_gauss()
