import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 1]

colors = np.random.rand(5)
sizes = np.random.rand(5) * 1000

plt.scatter(x, y, c=colors, cmap='jet', sizes=sizes, alpha=0.3)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Chart')
plt.show()
