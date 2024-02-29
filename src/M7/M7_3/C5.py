import pandas as pd

d = {'col1': [-1, 0, 5, -3, 6, 7, 0], 'col2': [5, 7, 3, 8, 4, 6, 5]}
df = pd.DataFrame(data=d)

df.corr()
