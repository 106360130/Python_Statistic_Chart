import pandas as pd
import seaborn as sns

# have no figure show on
# use "matplotlib.pyplot.show()"

# Reference
# https://www.delftstack.com/zh-tw/howto/seaborn/seaborn-plots-not-showing/
import matplotlib.pyplot as plt

df = pd.DataFrame([
    ['Jack', 78],
    ['Mary', 67],
    ['Mike', 90],
    ['David', 81],
], columns=['Students', 'Math'])

ax = sns.barplot(x='Students', y='Math', data=df)
ax.set_title('Final Term')

plt.show()