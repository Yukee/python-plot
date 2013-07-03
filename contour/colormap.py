import matplotlib
import matplotlib.colors as col
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

# cm.'colorname'._segmentdata : dictonary of the colormap. here we create our own _segmentdata dict. Still not sure how this works...
cdict = {'red': ((0.0, 0.0, 0.0),
                 (0.6, 1.0, 0.7),
                 (1.0, 1.0, 1.0)),
         'green': ((0.0, 0.0, 0.0),
                   (0.6, 1.0, 0.0),
                   (1.0, 1.0, 1.0)),
         'blue': ((0.0, 0.0, 0.0),
                  (0.6, 1.0, 0.0),
                  (1.0, 0.5, 1.0))}
my_cmap = col.LinearSegmentedColormap('my_colormap',cdict,256)
plt.pcolor(np.random.rand(10,10),cmap=my_cmap)
plt.colorbar()

plt.show()
