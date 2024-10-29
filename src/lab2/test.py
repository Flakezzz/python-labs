import math as m

a = 1.1
b = 3.5
h = 0.1
d = 0.001


def tab(x, d):
    sum = 0
    k = 1
    element = 2 * d
    while abs(element) > d:
        element = ((-1)*(k+1)) * m.cos(k * x) / ((x + 2**k)*3)
        sum += element
        k += 1
    return sum

x = a
while x <= b:
    result = tab(x, d)
    print(f"x = {x:.1f}, result = {result:.3f}")
    x += h