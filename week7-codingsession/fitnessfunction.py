import numpy as np
import matplotlib.pyplot as plt


def onemax(x):
    return x.sum()


class BitFlipMutation:

    def mutate(self, x):
        """
        Do Binary bit flip on a binary string. Pick a random
        index, and flip it's bit.
        """

        idx = np.random.randint(x.shape[0])
        xp = x.copy()
        xp[idx] = 1-x[idx]  # 1-1 = 0,0-1 = -1

        return xp


mutObj = BitFlipMutation()
x = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
xp = mutObj.mutate(x)
print(x)
print(xp)


def evolve(x, y, func, mutation, compare, archive):
    xp = mutation(x)
    yp = func(xp)

    if not y > yp:
        x = xp
        y = yp

        archive = []

        for gen in range(ngens):
            x, y, archive = evolve(x, y, func, mutation, compare, archive)

            return e, y, archive


print(x, y)
plt.figure()
plt.plot(archive)
