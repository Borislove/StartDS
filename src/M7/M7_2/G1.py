# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

# Read in data and examine first 10 rows
flights = pd.read_csv('numbers.csv')
flights.head(10)

"""
# matplotlib histogram
plt.hist(flights['arr_delay'], color='blue', edgecolor='black',
         bins=int(180 / 5))
"""

# seaborn histogram
sns.distplot(flights['arr_delay'], hist=True, kde=False,
             bins=int(180 / 5), color='blue',
             hist_kws={'edgecolor': 'black'})
# Add labels
#plt.title('Histogram of Arrival Delays')
#plt.xlabel('Delay (min)')
#plt.ylabel('Flights')
