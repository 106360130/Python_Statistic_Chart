import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([
    ['Jack', 78, 94],
    ['Mary', 67, 71],
    ['Mike', 90, 65],
    ['David', 81, 88],
], columns=['Students', 'Math', 'History'])
df_avg = (df['Math'] + df['History']) / 2
df_max = df[['Math', 'History']].max(axis=1)
df_min = df[['Math', 'History']].min(axis=1)
lower_errors = df_avg - df_min
upper_errors = df_max - df_avg
x = np.arange(len(df))

plt.bar(x, df_avg, color=['red', 'green', 'blue', 'yellow'], yerr=[lower_errors, upper_errors], capsize=5)
plt.xticks(x, df['Students'])
plt.xlabel('Students')
plt.ylabel('Math')
plt.title('Final Term')
plt.show()