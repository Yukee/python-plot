#!/usr/bin/env python
"""
usage: python ploy.py begin_index end_index skip dt
"""
from os import system
import pylab
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from sys import argv

# argv is the list of command-line arguments passed to this script (see usage)
a=int(argv[1])
counter=1
end=int(argv[2])
skip=int(argv[3])
dt=float(argv[4])

loadpath = '/home/nicolas/git/python-plot/animations/files/Flume2D1eq2_'
savepath = '/home/nicolas/git/python-plot/animations/results/contour_'

while (a + skip*(counter - 1)) < end:
    a1 = ('%05i' % counter)
    b = dt*(a + skip*(counter - 1))
    b1 = str(int(b))
    fig = plt.figure()

    # 
    matplotlib.rcParams['xtick.direction'] = 'out'
    matplotlib.rcParams['ytick.direction'] = 'out'
    
    # unpack = True transposes the returned array, so that x is the first column in the file, etc.
    x, y, z = np.loadtxt(loadpath + b1 + ".tsv", unpack = True)
    print('loaded file number ' + b1)
    min_x = np.min(x)
    max_x = np.max(x)
    min_y = np.min(y)
    max_y = np.max(y)
    
    xi = np.linspace(min_x, max_x, 200)
    yi = np.linspace(min_y, max_y, 200)
    # interpolates z(x,y) at points xi, yi using Delaunay triangulation ('nn' option)
    zi = mlab.griddata(x, y, z, xi, yi, interp = 'nn')
    
    levels = np.linspace(0.8, 1.2, 20)
    CS1 = plt.contourf(xi, yi, zi, levels, cmap = plt.cm.coolwarm, vmax = np.max(levels), vmin = np.min(levels))
    #CS2 = plt.contour(CS1, levels = CS1.levels[::2], colors = 'b', hold = 'on')
    CS2 = plt.contour(CS1, levels = [-0.001, 0.001], colors = 'b', hold = 'on')
    #plt.clabel(CS2, fmt = '%4.3f', colors = 'b', fontsize = 8)
    
    plt.xlabel('x')
    plt.ylabel('z')
    plt.title('Concentration of small particles in the centre plane')
    fig.colorbar(CS1)
    fig.savefig(savepath + a1 + '.png', bbox_inches = 0)

    plt.close()
    counter += 1

print 'Done plotting, generating video'
system('ffmpeg -qscale 5 -r 10 -b 9600 -i /home/nicolas/git/python-plot/animations/results/contour_%05d.png /home/nicolas/git/python-plot/animations/results/contour_video.avi')
system('vlc -L /home/nicolas/git/python-plot/animations/results/contour_video.avi')
