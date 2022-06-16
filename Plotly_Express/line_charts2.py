import pandas as pd
import plotly.express as px

df = pd.DataFrame([
    ['T', 2019, 150],
    ['T', 2020, 200],
    ['E', 2019, 170],
    ['E', 2020, 160],
    ['U', 2019, 200],
    ['U', 2020, 180],
], columns=['country', 'year', 'life'])

figure = px.line(df, x='year', y='life', color='country', title='Line Chart', line_dash='country')
figure.show()