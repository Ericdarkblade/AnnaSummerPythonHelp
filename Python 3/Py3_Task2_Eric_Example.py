# f = signal_array = []  # iterate with index i
# g = filter_array = []  # iterate with index j
# m = filter_array_length = 0

import math
import numpy as np
import \
    matplotlib.pyplot as plt  # Had to look up how to plot a graph from geeksforgeeks link: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/


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

    # You don't have to do this. You could initiate an empty list [] and instead of doing:
    # signal_array[i] = /* Your code here */
    # do
    # signal_array.append(/*Your code here*/) but I have a feeling that would be significantly
    # slower. I'm just not sure how python works.

    signal_array = [None] * length  # Initiates an array to have input length.
    for i in range(length):
        signal_array[i] = (math.sin(i / 500 * math.pi)) ** 2

    return signal_array


# These values were determined by the handout provided.
# These also have global scope and therefor are not a part of a function.

signal_array = generate_signal()  # again this just calls generate_signal with default value of 1000
filter_array = [1 / 16, 1 / 4, -3 / 8, 1 / 4, 1 / 16]

# I honestly have never used numpy or matplot lib, but I saw that this
# function existed. I was expecting to have to multiply by hand with own set loops. Oh, well.
convolution = np.convolve(signal_array, filter_array)

# Print that is required from the assignment handout. The first 10 values were requested.
for i in range(10):
    print(convolution[i])

# This is the extra credit part that I thought was interesting.

plt.plot(signal_array, label="Original Signal", color="red")
plt.plot(convolution, label="Convolved Signal", color="blue")  # I wonder if I can pass through rgb
plt.legend()

plt.xlabel("Signal Length")
plt.ylabel("Amplitude")

plt.title("Original Signal compared to Convolved Signal")
plt.show()
