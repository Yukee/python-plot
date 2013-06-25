#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

file = "phiinit.tsv"

fig = plt.figure()

x, y, z = np.genfromtxt(file, unpack = True, dtype = 'f8')

llc = np.array([-4.5,0])
xi = np.array([4.5,0.25])
nx = 4500
ny = 250

# domain
extent = np.transpose(np.array([llc, llc + xi]))
extent = extent.flatten()

zi = z.reshape(ny,nx)
xi = np.linspace(llc[0],llc[0]+xi[0],nx)
yi = np.linspace(llc[1],llc[1]+xi[1],ny)

levels = np.linspace(0.1, 1, 100)

# is this really useful?
norm = cm.colors.Normalize(vmax=zi.max(), vmin=zi.min())

# use interpolation='nearest' to plot the actual pixels
im = plt.imshow(zi, origin='lower', interpolation='nearest', extent=extent, cmap = cm.gist_ncar, norm=norm, aspect=4)

fig.colorbar(im, orientation='horizontal')

plt.show()
