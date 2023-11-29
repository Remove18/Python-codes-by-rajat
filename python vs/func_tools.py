from functools import lru_cache as lc
from time import sleep as s

@lc(maxsize=None)
def num(n, m):
    s(5)
    return n*m

print(num(1873478294576348524,1632762742435872548732466))

print(num(1873478294576348524,1632762742435872548732466))

print(num(1873478294576348524,1632762742435872548732466))