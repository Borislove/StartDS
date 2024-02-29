import numpy as np

import seaborn as sns

height = np.array([100, 130, 95, 115, 80])  # рост
weight = np.array([15, 18, 12, 17, 9])  # вес

corr = np.corrcoef(height, weight)

sns.regplot(x=5, y=5)

# Equivalent to:
sns.regplot(x="x", y="y", data=corr)
