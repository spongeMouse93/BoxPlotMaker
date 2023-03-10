import numpy as np
import matplotlib.pyplot as plt

fileName = input("Enter the name of file containing sample data: ")
try:
  data = []
  with open(fileName, 'r') as file:
    numElements = int(file.readLine())
    for i in range(numElements):
      data.append(int(file.readLine())
  plt.boxplot(data, vert = 0)
  plt.show()
  data.sort()
  print("Smallest element: " + str(data[0]))
  print("Largest element: " + str(data[len(data) - 1]))
  print("First quartile: " + str(np.quantile(data, 0.25)))
  print("Median: " + str(np.quantile(data, 0.5)))
  print("Third quartile: " + str(np.quantile(data, 0.75)))
  print("Interquartile range: " + str(np.quantile(data, 0.75) - np.quantile(data, 0.25)))
except FileNotFoundError:
  print("Error: File Not Found")
