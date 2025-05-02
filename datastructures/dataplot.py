import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function
def f(x, y):
    frac1 = -(x - 3)**2 / 5
    frac2 = -(y - 1)**2 / 10
    return 10 * np.exp(frac1 + frac2)

# Create grid
x = np.linspace(-2, 8, 100)
y = np.linspace(-4, 6, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.title('Surface Plot of f(x, y)')
plt.show()