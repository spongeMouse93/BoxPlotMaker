import numpy as np
import matplotlib.pyplot as plt

numElements = int(input("How many elements? "))
data = []
for i in range(numElements):
    x = int(input("Element #" + str(i) + ": "))
    data.append(x)
plt.boxplot(data, vert = 0)
plt.show()
data.sort()
print("Smallest element: " + str(data[0]))
print("Largest element: " + str(data[len(data) - 1]))
print("First quartile: " + str(np.quantile(data, 0.25)))
print("Median: " + str(np.quantile(data, 0.5)))
print("Third quartile: " + str(np.quantile(data, 0.75)))
print("Interquartile range: " + str(np.quantile(data, 0.75) - np.quantile(data, 0.25)))
