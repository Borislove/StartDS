import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns

import pandas as pd
from sklearn.datasets import load_diabetes
import seaborn as sns
import matplotlib.pyplot as plt

# корреляция
height = np.array([100, 130, 95, 115, 80])  # рост
weight = np.array([15, 18, 12, 17, 9])  # вес


# x = np.array([1,3,5,7,8,9, 10, 15])
# y = np.array([10, 20, 30, 40, 50, 60, 70, 80])


def Pearson_correlation(X, Y):
    if len(X) == len(Y):
        Sum_xy = sum((X - X.mean()) * (Y - Y.mean()))
        Sum_x_squared = sum((X - X.mean()) ** 2)
        Sum_y_squared = sum((Y - Y.mean()) ** 2)
        corr = Sum_xy / np.sqrt(Sum_x_squared * Sum_y_squared)
    return corr


# print(Pearson_correlation(height, weight))
# print(Pearson_correlation(height, height))


print(np.corrcoef(height, weight))
corr = np.corrcoef(height, weight)

# Load the dataset with frame
df = load_diabetes(as_frame=True)
# conver into pandas dataframe
df = df.frame
# Print first 5 rows
df.head()

plt.figure(figsize=(10, 8), dpi=500)
sns.heatmap(np.corrcoef(height, weight), annot=True, fmt=".2f", linewidth=.5)
plt.show()

matplotlib.pyplot.imshow

"""
matplotlib.pyplot.imshow(X, cmap=None, norm=None, *, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None,
                         origin=None, extent=None, interpolation_stage=None, filternorm=True, filterrad=4.0,
                         resample=None, url=None, data=None, **kwargs)[source]
"""


