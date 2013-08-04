#!/usr/bin/env python

from os import system
import matplotlib
import matplotlib.colors as col
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import sys
from sys import argv

if len(argv) < 2 : sys.exit('usage: "python plot.py filename" (without .tsv)')

file = argv[1] + '.tsv'

fig = plt.figure()

zi = np.genfromtxt(file, dtype = 'f8')

levels = np.linspace(0, 99, 2)

# is this really useful?
norm = cm.colors.Normalize(vmax=99, vmin=0)

# use interpolation='nearest' to plot the actual pixels
im = plt.imshow(zi, origin='lower', interpolation='nearest', cmap = cm.RdYlGn, norm=norm, aspect=1)

fig.colorbar(im, orientation='vertical')

plt.show()

#fig.savefig(file + '.png', bbox_inches = 0, dpi=1000)
