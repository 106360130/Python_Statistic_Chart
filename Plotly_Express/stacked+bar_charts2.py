import pandas as pd
import plotly.express as px

df = pd.DataFrame([
    ['Jack', 78, 94],
    ['Mary', 67, 71],
    ['Mike', 90, 65],
    ['David', 81, 88],
], columns=['Students', 'Math', 'History'])

figure = px.bar(df, x='Students', y=['Math', 'History'], title='Final Term')
figure.show()