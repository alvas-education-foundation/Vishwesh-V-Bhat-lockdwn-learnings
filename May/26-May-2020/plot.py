import numpy as np
import matplotlib.pyplot as plot
from matplotlib.cm import get_cmap



dx = 0.001
L = np.pi
x = L * np.arange(-1+dx,1+dx,dx)
n = len(x)
nquart = int(np.floor(n/4))

f=np.zeros_like(x)
f[nquart:2*nquart] = (4/n)*np.arange(1,nquart+1)
f[2*nquart:3*nquart] = np.ones(nquart) - (4/n)*np.arange(0,nquart)

ax = plt.subplots()
ax.plot(x,f,'-',color='k',LineWidth=2)

name = 'Accent'
cmap = get_cmap("tab10")
colors = cmap.colors
ax.set_prop_cycle(color=colors)

A0 = np.sum(f * np.ones_like(x)) * dx
fFS = A0/2

A = np.zeros(20)
B = np.zeros(20)
for k in range(20):
    A[k]=np.sum(f * np.cos(np.pi*(k+1)*x/L)) * dx
    B[k]=np.sum(f * np.sin(np.pi*(k+1)*x/L)) * dx
    fFS = fFS + A[k]*np.cos((k+1)*np.pi*x/L) + B[k]*np.sum((k+1)*np.pi*x/L)
    ax.plot(x,fFS,'-')