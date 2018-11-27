from random import *


def randBinList(n):
    return [randint(0, 1) for _ in range(1, n + 1)]


def fitBits(desired, real):
    return desired == real


def main():
    bits = randBinList(5)
    print(bits)


main()
