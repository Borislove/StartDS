import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('numbers.csv', sep=',', header=None, index_col=0)
# numbers = np.loadtxt("numbers.csv", delimiter=",")
data.plot(kind='bar')
plt.ylabel('Frequency')
plt.xlabel('Words')
plt.title('Title')
plt.show()
