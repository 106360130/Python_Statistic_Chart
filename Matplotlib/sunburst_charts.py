import pandas as pd
import matplotlib.pyplot as plt

# item and number
df = pd.DataFrame([
    ['France', 61083916, 'Europe'], ['Germany', 82400996, 'Europe'], ['Italy', 58147733, 'Europe'],
    ['Spain', 40448191, 'Europe'], ['United Kingdom', 60776238, 'Europe'], ['Taiwan', 23174294, 'Asia'],
    ['Japan', 127467972, 'Asia'], ['Korean', 49044790, 'Asia'], ['China', 1318683096, 'Asia']],
    columns=['country', 'pop', 'continent'])
# item and number

europe_sum = df[df['continent']=='Europe']['pop'].sum()
asia_sum = df[df['continent']=='Asia']['pop'].sum()
fig, ax = plt.subplots()
size = 0.4
ax.pie(df['pop'], labels=df['country'],
       autopct='%1.2f%%', pctdistance=0.8,
       radius=1, wedgeprops=dict(width=size, edgecolor='w'))
ax.pie([europe_sum, asia_sum], labels=['Europe', 'Asia'], labeldistance=0.2,
       autopct='%1.2f%%', pctdistance=0.6,
       radius=1-size, wedgeprops=dict(width=size, edgecolor='w'))
plt.title('Population')
plt.show()