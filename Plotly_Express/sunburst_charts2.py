import pandas as pd
import plotly.express as px

df = pd.DataFrame([
    ['Europe', 586098529, 'Total'], ['Asia', 3811953827, 'Total'],
    ['France', 61083916, 'Europe'], ['Germany', 82400996, 'Europe'], ['Italy', 58147733, 'Europe'],
    ['Spain', 40448191, 'Europe'], ['United Kingdom', 60776238, 'Europe'], ['Taiwan', 23174294, 'Asia'],
    ['Japan', 127467972, 'Asia'], ['Korean', 49044790, 'Asia'], ['China', 1318683096, 'Asia']],
    columns=['country', 'pop', 'continent'])

fig = px.sunburst(df, names='country', values='pop', parents='continent', title='Population')
fig.show()