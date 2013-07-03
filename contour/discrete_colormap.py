""" base code from http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps """

import matplotlib
import matplotlib.colors as col
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

"""create a colormap with N (N<8) discrete colors and register it"""
def discrete_cmap(N=7):
    # define individual colors as hex values
    cpool = [ '#FF6E30', '#D05A27', '#AA4920', '#883A19', '#662C13',
              '#311509', '#000000']

    # TODO: build cpool as a sequence of colors of variying value (from 0 to 255) in hsv color space, then convert to hex

    discrete_cmap = col.ListedColormap(cpool[0:N], 'discrete_copper')
    cm.register_cmap(cmap=discrete_cmap)

"""display all colormaps included in the names list. If names is None, all
defined colormaps will be shown."""
def show_cmaps(names=None):
    matplotlib.rc('text', usetex=False)
    a=np.outer(np.arange(0,1,0.01),np.ones(10))   # pseudo image data
    f=plt.figure(figsize=(10,5))
    f.subplots_adjust(top=0.8,bottom=0.05,left=0.01,right=0.99)
    # get list of all colormap names
    # this only obtains names of built-in colormaps:
    maps=[m for m in cm.datad if not m.endswith("_r")]
    # use undocumented cmap_d dictionary instead
    maps = [m for m in cm.cmap_d if not m.endswith("_r")]
    maps.sort()
    # determine number of subplots to make
    l=len(maps)+1
    if names is not None: l=len(names)  # assume all names are correct!
    # loop over maps and plot the selected ones
    i=0
    for m in maps:
        if names is None or m in names:
            i+=1
            ax = plt.subplot(1,l,i)
            ax.axis("off")
            plt.imshow(a,aspect='auto',cmap=cm.get_cmap(m),origin="lower")
            plt.title(m,rotation=90,fontsize=10,verticalalignment='bottom')
    plt.savefig("colormaps.png",dpi=100,facecolor='gray')

if __name__ == "__main__":

    discrete_cmap(7)
    show_cmaps(['indexed'])
