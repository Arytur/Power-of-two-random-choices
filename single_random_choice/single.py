from collections import defaultdict

import numpy as np
from plot import display_histogram

from const import NR_OF_BINS, NR_OF_BALLS

BINS = defaultdict(list)


def select_random_bin() -> int:
    return np.random.randint(1, NR_OF_BINS + 1)


def assign_balls_to_bins():
    for ball_number in range(1, NR_OF_BALLS + 1):
        selected_bin: int = select_random_bin()
        BINS[selected_bin].append(ball_number)


assign_balls_to_bins()
display_histogram(BINS)
