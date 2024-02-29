import statistics

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display

df = pd.read_csv("pop.csv", delimiter=';')
# df = pd.read_csv("https://raw.githubusercontent.com/aiedu-courses/all_datasets/main/Population.csv", delimiter=';')
# plt.legend()

# df.head()

# печать всех
# print(df.to_string())

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
display(df.head())

years = df.columns[1:].astype(int)
print(years[-5:])
years[-5:]

aruba_population = df[df['Country Name'] == 'Bulgaria'].values[0][1:]  # 8120173
# aruba_population = df[df['Country Name'] == 'Aruba'].values[0][1:]  #77456
# aruba_population = df[df['Country Name'] == 'Eritrea'].values[0][1:]  #2181781
# aruba_population = df[df['Country Name'] == 'Germany'].values[0][1:]  #79733486
# aruba_population = df[df['Country Name'] == 'Kosovo'].values[0][1:]  #1601582
# aruba_population = df[df['Country Name'] == 'Dominican Republic'].values[0][1:]  #7266056
# aruba_population = df[df['Country Name'] == 'Croatia'].values[0][1:]  # 4406813
print(aruba_population[:5])
aruba_population[:5]

# plt.plot(years, aruba_population, '-')

# median
print("Median")
print(np.median(aruba_population))
plt.plot(years, aruba_population, '-')
# среднее значение
print('Среднее значение:')
print(round(statistics.mean(aruba_population)))
# plt.show()

# test
