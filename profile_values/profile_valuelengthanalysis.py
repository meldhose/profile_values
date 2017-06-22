"""Analysing the value lengths by histogram"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def histogram_value_lengths(data_frame):
    """
    Returns histogram on length of values in DataFrame.
    Args:
        data_frame (pandas DataFrame): Input pandas DataFrame
    Returns:
        histogram ()
    """
    col_title = data_frame.columns.get_values()[0]
    data_frame['Length'] = data_frame[col_title].str.len()
    plt.hist(data_frame['Length'], bins=100)
    histogram = plt.show()
    return histogram

