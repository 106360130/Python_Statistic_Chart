import pandas as pd
import plotly.express as px

df = pd.DataFrame([
    ['Asia', 'T', 120, 150],
    ['Asia', 'J', 150, 100],
    ['Europe', 'E', 150, 200],
    ['Europe', 'F', 200, 150],
    ['Americas', 'U', 250, 150],
    ['Americas', 'M', 70, 100],
], columns=['continent', 'country', 'gdp', 'life'])

figure = px.scatter(df, x='gdp', y='life',
                    color='continent', title='Scatter Chart',
                    hover_name='country', symbol='country',
                    size='life', size_max=20)

figure.show()