import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 1],
], columns=['x', 'y'])

plt.plot('x', 'y', 'bs', data=df, label="s")
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Chart')
plt.show()