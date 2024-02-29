import matplotlib.pyplot as plt
import pandas as pd

#students = pd.read_csv("StudentsPerformance.csv")
students = pd.read_csv("StudentsPerformance.csv")

plt.hist(students["math score"], label="Тест по математике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()