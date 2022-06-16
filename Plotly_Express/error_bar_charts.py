import pandas as pd
import plotly.express as px

df = pd.DataFrame([
    ['Jack', 78, 94],
    ['Mary', 67, 71],
    ['Mike', 90, 65],
    ['David', 81, 88],
], columns=['Students', 'Math', 'History'])

df_avg = (df['Math'] + df['History']) / 2
df_max = df[['Math', 'History']].max(axis=1)
df_min = df[['Math', 'History']].min(axis=1)

figure = px.bar(df,
                x='Students',
                y=df_avg,
                error_y=df_max-df_avg,
                error_y_minus=df_avg-df_min,
                title='Final Term')

figure.show()