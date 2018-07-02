import numpy as np
import random


def all_possibilities(n):
    pass


def simulate(n, epochs=1000, verbose=False):
    results = []
    for _ in range(epochs):
        houses = np.repeat('_', n)

        while '_' in houses:
            i = random.randrange(n)
            if houses[i] == '_':
                houses[i] = 'X'
                if i + 1 < n:
                    houses[i + 1] = 'O'
                if i - 1 >= 0:
                    houses[i - 1] = 'O'
        if verbose:
            results.append(houses)
        else:
            unique, counts = np.unique(houses, return_counts=True)
            try:
                results.append(dict(zip(unique, counts))["X"])
            except KeyError:
                results.append(0)
    if verbose:
        return results
    else:
        return np.average(results)


def calculate(n):
    houses = np.repeat('_', n)


if __name__ == '__main__':
    for i in range(50):
        print(simulate(100) / 100)  # this gives answer of ~0.42 %.






