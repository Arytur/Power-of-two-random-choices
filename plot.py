from matplotlib import pyplot as plt
import numpy as np


def display_histogram(bins):
    bins_lengths = []
    for k, v in bins.items():
        bins_lengths.append(len(v))

    counts, bins = np.histogram(bins_lengths)
    print(counts, bins)
    print(np.std(bins))
    plt.stairs(counts, bins)
    plt.show()

