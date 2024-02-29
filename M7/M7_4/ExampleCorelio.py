
import statistics

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display

# кореляция между Болгарией и Хорватией
df = pd.read_csv("pop.csv", delimiter=';')


aruba_population = df[df['Country Name'] == 'Aruba'].values[0][1:]  #77456
croatia_population = df[df['Country Name'] == 'Croatia'].values[0][1:]  # 4406813

# median
print("Median")
print(np.median(aruba_population))

# среднее значение
print('Среднее значение:')
print(round(statistics.mean(aruba_population)))
# plt.show()


# пик населения!!!
df = df.set_index('Country Name')
print(df.loc['Croatia'].idxmax())

#print(aruba_population.corr(croatia_population))
correlation = df["sepal length (cm)"].corr(df["petal length (cm)"])