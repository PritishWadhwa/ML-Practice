# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import matplotlib.pylab as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# %%
# a = np.array([1,2,3])
# b = np.array([4,5,6,7])
a = np.arange(-1, 1, 0.02)
b = a
a, b = np.meshgrid(a, b)
# meshgrid repeats a along rows n(b) number of times and repeats b along column n(a) number of times
# a and b together form a 2d plane/surface where the x coord is from a and y coord is from b


# %%
print(a)
print(b)


# %%
fig = plt.figure()
axes = fig.gca(projection='3d')  # gives me axis in 3d
# axes.plot_surface(a, b, a+b, cmap = 'coolwarm') # (x, y, z)
axes.plot_surface(a, b, a**2+b**2, cmap='rainbow')  # (x, y, z)
plt.show()


# %%
fig = plt.figure()
axes = fig.gca(projection='3d')
axes.contour(a, b, a**2+b**2, cmap='coolwarm')
plt.show()


# %%
