import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    ['Jack', 78],
    ['Mary', 67],
    ['Mike', 90],
    ['David', 81],
], columns=['Students', 'Math'])

fig = px.bar(df, x='Students', y='Math', title='Final Term')
fig.show()