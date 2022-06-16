import pandas as pd
import plotly.express as px

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

fig = px.bar(df, x='Students', y='Scores', color='Class', barmode='group', title='Final Term')
fig.show()