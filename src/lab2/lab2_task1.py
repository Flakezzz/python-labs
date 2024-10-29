import math as m
import numpy as np


def func1(x):
    return m.log(3*x + 1, 5)
def func2(x):
    return x**m.cos(x)
def func3(x):
    return 1/m.sin(m.log(x, np.e))


a = 0.1
b = 0.7
h = 0.05

while a <= b + h:
    if a < 0.2:
        print(f"x = {a:.2f}, res = {round(func1(a), 3)}")
    elif 0.2 <= a < 0.4:
        print(f"x = {a:.2f}, res = {round(func2(a), 3)}")
    else:
        print(f"x = {a:.2f}, res = {round(func3(a), 3)}")
    a += h