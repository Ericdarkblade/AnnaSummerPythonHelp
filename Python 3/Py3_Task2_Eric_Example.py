# f = signal_array = []  # iterate with index i
# g = filter_array = []  # iterate with index j
# m = filter_array_length = 0

import math, NumPy


# NOTE there was big error in the example provided in the handout see explanation here:
# https://i.imgur.com/DN8L023.png


# Note this function is not required, but I made it out of good practice so that you could have modular length signals.
def generate_signal(length=1000):
    """
    Generates a signal according to the formula:
    f[i] = sin^2(i/500 * pi)

    Default length is 1000.

    Args:
        length (int): the length of the signal array to be generated. Defaults to 1000.

    Returns:
        signal_array (float array): the singal array generated from the formula of length length.
    """
    signal_array = []
    for i in range(length):
        signal_array[i] = (math.sin(i / 500 * math.pi)) ** 2

    return signal_array


# These values were determined by the handout provided.
# These also have global scope and therefor are not a part of a function.
filter_array = [1 / 16, 1 / 4, -3 / 8, 1 / 4, 1 / 16]

##WIP