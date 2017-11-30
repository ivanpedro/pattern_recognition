"""
First we need to know how we can obtain the samples of a pure tone. The following
code does this when we have defined the variables f for its frequency, antsec
for its length in seconds, and fs for the sampling rate.

fs (the sampling frequency or sampling rate) measurements /s, 44 100 16 bit cd, 192 000 dvd 24bit
"""

import numpy as np
from mpmath import linspace
from scipy.io.matlab.tests.test_streams import fs
from math import *

fs = 44100
f = 440
antsec = 10
# Create samples of a pure tone
t = np.linspace(0, antsec, fs*antsec)
x = np.sin(2*pi*f*t)

print (t)
print(x)