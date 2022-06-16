import pandas as pd
import seaborn as sns

# have no figure show on
# use "matplotlib.pyplot.show()"

# Reference
# https://www.delftstack.com/zh-tw/howto/seaborn/seaborn-plots-not-showing/
import matplotlib.pyplot as plt

df = pd.DataFrame([
    ['Jack', 'Math', 78],
    ['Jack', 'History', 94],
    ['Mary', 'Math', 67],
    ['Mary', 'History', 71],
    ['Mike', 'Math', 90],
    ['Mike', 'History', 65],
    ['David', 'Math', 81],
    ['David', 'History', 88],
], columns=['Students', 'Class', 'Scores'])


ax = sns.barplot(x='Students', y='Scores', hue='Class', data=df)
ax.set_title('Final Term')

plt.show()

