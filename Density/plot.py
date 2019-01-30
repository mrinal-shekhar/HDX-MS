import numpy as np
import numpy as np
from matplotlib.colors import LogNorm
from matplotlib import pyplot as pl
from pylab import pcolor, show, colorbar, xticks, yticks
import numpy as np
from matplotlib import pyplot as pl
import matplotlib.ticker as ticker
from matplotlib import rc
import matplotlib
from random import uniform
import math
from scipy.stats import gaussian_kde
#matplotlib.use('Cairo')

import matplotlib.pyplot as pl

from matplotlib import rc
import matplotlib
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}",r"\renewcommand{\seriesdefault}{\bfdefault}",
r"\usepackage{amsfonts}", r"\usepackage{textgreek}",r"\usepackage{textcomp}",r"\usepackage{gensymb}",
r"\usepackage{fixltx2e}", r'\boldmath'] #Using \boldmath makes the axis label numbers bold as well! Looks #good.
params = {'text.usetex' : True,
          'font.size' : 18,
          'font.family' : 'lmodern',
          'text.latex.unicode': True,
          'figure.figsize' : (15, 8), #8, 6 originally. Make it ~30% smaller so the text is ~30% #bigger. (Multiply by .7)
         'figure.dpi' : 120,
          'figure.autolayout' : True
          }
matplotlib.rcParams.update(params)

matplotlib.rcParams.update(params)

fig, ax = pl.subplots()


x=np.genfromtxt('x.dat')
y=np.genfromtxt('y.dat')
x=x[~np.isnan(x)] 
y=y[~np.isnan(y)] 
#weights = np.ones_like(f[0:,1])/(2198.0)

pl.hist2d(x,y,bins=(150,150),cmap=pl.cm.hot)
cl=pl.colorbar()

pl.xlim(-50,50)
pl.ylim(-50,50)
pl.xlabel("X-axis")
pl.ylabel("Y-axis")

pl.savefig('density.png')
