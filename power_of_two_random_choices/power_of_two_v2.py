from collections import defaultdict

import numpy as np

from const import NR_OF_BINS, NR_OF_BALLS
from plot import display_histogram

BINS = defaultdict(list)


def select_random_bin() -> int:
    return np.random.randint(1, NR_OF_BINS + 1)


def select_bin() -> int:
    bin_1 = select_random_bin()
    bin_2 = select_random_bin()
    while bin_1 == bin_2:
        bin_2 = select_random_bin()
    return bin_1 if len(BINS[bin_1]) < len(BINS[bin_2]) else bin_2


def assign_balls_to_bins():
    for ball_number in range(1, NR_OF_BALLS + 1):
        selected_bin: int = select_bin()
        BINS[selected_bin].append(ball_number)


assign_balls_to_bins()
display_histogram(BINS)
