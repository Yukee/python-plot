#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from numpy import ma

'''
X,Y = np.meshgrid( np.arange(0,2*np.pi,.2),np.arange(0,2*np.pi,.2) )
U = np.cos(X)
V = np.sin(Y)
'''

file = "uinit.tsv"
x, y, U, V = np.genfromtxt(file, unpack = True, dtype = 'f8')

llc = np.array([-4.5,0])
xi = np.array([4.5,0.25])
nx = 4500
ny = 250

# domain
extent = np.transpose(np.array([llc, llc + xi]))
extent = extent.flatten()

Ui = U.reshape(ny,nx)
Vi = V.reshape(ny,nx)
xi = np.linspace(llc[0],llc[0]+xi[0],nx)
yi = np.linspace(llc[1],llc[1]+xi[1],ny)

plt.figure()
Q = plt.quiver(xi, yi, Ui, Vi)

# use this if you want to label the arrow. Origin of the coordinate system is at the lower left corner
qk = plt.quiverkey(Q, 0.5, 0.92, 2, r'$2 \frac{m}{s}$', labelpos='W', fontproperties={'weight': 'bold'})

# workaround to take the arrows into account when plotting
l,r,b,t = plt.axis()
dx, dy = r-l, t-b
plt.axis([l-0.05*dx, r+0.05*dx, b-0.05*dy, t+0.05*dy])

plt.title('Minimal arguments, no kwargs')

plt.show()

