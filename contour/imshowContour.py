#!/usr/bin/env python

import matplotlib
import matplotlib.colors as col
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import sys
from sys import argv
from matplotlib.gridspec import GridSpec

"""create a colormap with N (N<8) discrete colors and register it"""
def discrete_cmap(N=14):
    # define individual colors as hex values
    cpool = [ '#FFC57E', '#FFB573', '#FEA167', '#EE9760', '#D88758', '#BF794D', '#A66943', '#8F5A39', '#76492E', '#5F3C26', '#492D1D', '#2F1D13',
              '#1A0F0A', '#000000']
    cpool = cpool[::-1]

    # TODO: build cpool as a sequence of colors of variying value (from 0 to 255) in hsv color space, then convert to hex

    discrete_cmap = col.ListedColormap(cpool[0:N], 'discrete_copper')
    cm.register_cmap(cmap=discrete_cmap)

discrete_cmap()

if len(argv) < 2 : sys.exit('usage: "python imshowContour.py filename" (without .tsv)')

file = argv[1] + '.tsv'

fig = plt.figure()

#ax = plt.subplot2grid((1,1), (0,0), colspan=1, rowspan=1)

x, y, z = np.genfromtxt(file, unpack = True, dtype = 'f8')

llc = np.array([-5,0])
xi = np.array([5,0.25])
nx = 250
ny = 125

# domain
extent = np.transpose(np.array([llc, llc + xi]))
extent = extent.flatten()

zi = z.reshape(ny,nx)
xi = np.linspace(llc[0],llc[0]+xi[0],nx)
yi = np.linspace(llc[1],llc[1]+xi[1],ny)

levels = np.linspace(0.03, 1, 50)

# is this really useful?
norm = cm.colors.Normalize(vmax=0.7, vmin=0.5)

# use interpolation='nearest' to plot the actual pixels
im = plt.contourf(zi, origin='lower', interpolation='nearest', extent=extent, cmap = cm.copper, norm=norm, aspect=4, levels=levels)

#im = ax.contourf(zi, origin='lower', interpolation='nearest', extent=extent, cmap = cm.copper, norm=norm, aspect=4, levels=levels)

fig.colorbar(im, orientation='horizontal')

plt.show()
