import pandas as pd
import seaborn as sns

# have no figure show on
# use "matplotlib.pyplot.show()"

# Reference
# https://www.delftstack.com/zh-tw/howto/seaborn/seaborn-plots-not-showing/
import matplotlib.pyplot as plt

df = pd.DataFrame([
    ['Asia', 'T', 120, 150],
    ['Asia', 'J', 150, 100],
    ['Europe', 'E', 150, 200],
    ['Europe', 'F', 200, 150],
    ['Americas', 'U', 250, 150],
    ['Americas', 'M', 70, 100],
], columns=['continent', 'country', 'gdp', 'life'])

ax = sns.scatterplot(x='gdp', y='life', data=df,
                     hue='continent', style='continent', palette='Set2',
                     size='continent', sizes=(20, 100))
ax.set_title('Scatter Chart')

plt.show()