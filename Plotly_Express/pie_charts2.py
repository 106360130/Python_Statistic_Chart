# ModuleNotFoundError: No module named 'plotly'
# pip install plotly

# Reference
# https://www.statology.org/no-module-named-plotly/

# it will show on the Internet
import pandas as pd
import plotly.express as px

df = pd.DataFrame([
    ['Czech Republic', 10228744], ['France', 61083916], ['Germany', 82400996],
    ['Greece', 10706290], ['Italy', 58147733], ['Netherlands', 16570613],
    ['Poland', 38518241], ['Portugal', 10642836], ['Romania', 22276056],
    ['Spain', 40448191], ['Turkey', 71158647], ['United Kingdom', 60776238]],
    columns=['country', 'pop'])

fig = px.pie(df, values='pop', names='country', title='Population')
fig.show()