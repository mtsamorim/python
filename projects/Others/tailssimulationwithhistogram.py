import numpy as np
import matplotlib.pyplot as plt

final_results = []

for x in range(10000):

    results = [0]

    for x in range(10):
        coin = np.random.randint(0, 2)
        results.append(results[x] + coin)

    final_results.append(results[-1])

plt.hist(final_results, bins=10)

plt.show()
