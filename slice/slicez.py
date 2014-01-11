#!/usr/bin/env python
"""
usage: python slice.py filename nx ny nz yvalue
"""
import numpy as np
from sys import argv
import matplotlib.pyplot as plt

filename = argv[1]
nx = int(argv[2])
ny = int(argv[3])
nz = int(argv[4])
i = int(argv[5])

phi = np.genfromtxt(filename + '.tsv', dtype='d8', unpack=True)[3]

phi = phi.transpose()

phi = phi[i:i*nx*ny]

plt.imshow(phi, origin='lower', interpolation='nearest')

plt.show()
