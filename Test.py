import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 25)

n = np.array([1,2,3,4,5])

fig, axes = plt.subplots(1, 4, figsize=(16, 10))

axes[0].set_title('Scatter plot')
axes[0].scatter(x, x + 0.25 * np.random.rand(len(x)))