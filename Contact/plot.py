import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
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

f=np.genfromtxt('contacts_all.txt', delimiter=',')
y_axis=f[:,1]
x_axis=f[:,0]
y_axis=f[:,1]/max(y_axis)	
label=list((x_axis))
index = np.arange(len(label))

plt.bar(label, y_axis,width=1,color='blue',alpha=0.5)
plt.xlabel('Residue id', fontsize=50)
plt.ylabel('Contact count', fontsize=50)

plt.grid()

plt.savefig('contact.png')

