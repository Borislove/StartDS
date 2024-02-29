import matplotlib.pyplot as plt
import pandas as pd

# рабочий гистограмма

data = pd.read_csv('numbers.csv', header=None, quoting=2)

# data.hist(bins=10)  # что за бины?
# data.hist(bins=9)
#n, bin, patches = plt.hist(data, bins=20)
index = [0,1,2,3,4]
values = [5,7,3,4,6]
plt.bar(index,values)
plt.show()

# plt.xlim([0, 100])
# plt.ylim([50, 500])
# plt.title("Data")
# plt.xlabel("lol")
# plt.ylabel("Frequency")
plt.show()
