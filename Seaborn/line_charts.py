import pandas as pd
import seaborn as sns

# have no figure show on
# use "matplotlib.pyplot.show()"

# Reference
# https://www.delftstack.com/zh-tw/howto/seaborn/seaborn-plots-not-showing/
import matplotlib.pyplot as plt

df = pd.DataFrame([
    ['T', 2019, 150],
    ['T', 2020, 200],
    ['E', 2019, 170],
    ['E', 2020, 160],
    ['U', 2019, 200],
    ['U', 2020, 180],
], columns=['country', 'year', 'life'])

ax = sns.lineplot(x='year', y='life', data=df.query('country=="T"'))
ax.set_title('Line Chart')

plt.show()