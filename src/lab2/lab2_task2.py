import math as m

def func1(x, k):
    return (1/2**k) * m.sin(x/2**k)
        
h = 0.1
d = 0.001
k = 1
x = 1.1     
res = 0

while x <= 2 + h:
    while m.fabs(func1(x, k) >= d):
        res += func1(x, k)
        k += 1
    print(f"x = {x:.1f}, sum = {res}")
    k = 0
    x += h