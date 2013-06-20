#!/usr/bin/env python
"""
decription: load images from text, print them in png files, build video from images using avconv
usage: python ploy.py begin_index end_index skip dt
"""
from os import system
import pylab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sys import argv

# argv is the list of command-line arguments passed to this script (see usage)
a=int(argv[1])
counter=1
end=int(argv[2])
skip=int(argv[3])
dt=float(argv[4])

filename = 'longrun_20fps_'
loadpath = 'files/' + filename
savepath = 'results/contour_' + filename

llc = np.array([-1.5,0])
xi = np.array([3,1])

# domain
extent = np.transpose(np.array([llc, llc + xi]))
extent = extent.flatten()

while (a + skip*(counter - 1)) < end:
    a1 = ('%05i' % counter)
    b = dt*(a + skip*(counter - 1))
    b1 = str(int(b))
    fig = plt.figure()
    
    # unpack = True transposes the returned array, so that x is the first column in the file, etc.
    x, y, z = np.genfromtxt(loadpath + b1 + ".tsv", unpack = True, dtype = 'f8')
    print('loaded file number ' + b1)

    zi = z.reshape(201,301)
    xi = np.linspace(llc[0],llc[0]+xi[0],301)
    yi = np.linspace(llc[1],llc[1]+xi[1],201)    

    levels = np.linspace(0, 1, 100)

    # is this really useful?
    norm = cm.colors.Normalize(vmax=zi.max(), vmin=zi.min())
    
    #plt.xlabel('x')
    #plt.ylabel('z')
    #plt.title('Concentration of small particles in the centre plane')

    # use interpolation='nearest' to plot the actual pixels
    im = plt.imshow(zi, origin='lower', interpolation='nearest', extent=extent, cmap = cm.gist_heat, norm=norm)

    fig.colorbar(im, orientation='horizontal')

    fig.savefig(savepath + a1 + '.png', bbox_inches = 0)

    plt.close()
    counter += 1

print 'Done plotting, generating video'
system('avconv -qscale 5 -r 10 -b 32k -i ' + savepath + '%05d.png ' + savepath + '.avi')
