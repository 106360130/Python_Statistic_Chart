import pandas as pd
import matplotlib.pyplot as plt

# item and number
df = pd.DataFrame([
    ['Czech Republic', 10228744], ['France', 61083916], ['Germany', 82400996],
    ['Greece', 10706290], ['Italy', 58147733], ['Netherlands', 16570613],
    ['Poland', 38518241], ['Portugal', 10642836], ['Romania', 22276056],
    ['Spain', 40448191], ['Turkey', 71158647], ['United Kingdom', 60776238]],
    columns=['country', 'pop'])
# item and number

plt.pie(df['pop'], labels = df['country'], autopct = '%1.2f%%')
plt.title('Population')
plt.show()