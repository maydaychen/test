import json
from numpy import *;
from matplotlib import *;
import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Squre of Value", fontsize=14)
#
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]
# plt.scatter(x_value, y_value, c='red', edgecolors='none', s=200)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Squre of Value", fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)

x_value = list(range(1001))
y_value = [x ** 2 for x in x_value]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.savefig('squares_plot.png', bbox_inches='tight')
