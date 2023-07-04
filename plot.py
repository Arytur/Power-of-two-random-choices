from matplotlib import pyplot as plt
import numpy as np


def display_histogram(bins):
    bins_lengths = []
    for k, v in bins.items():
        bins_lengths.append(len(v))

    counts, bins = np.histogram(bins_lengths)
    print(counts, bins)
    # std_values = [67.04028639556964, 2.213594362117859, 1.8973665961010209]
    print(np.std(bins))
    plt.stairs(counts, bins)
    plt.show()

