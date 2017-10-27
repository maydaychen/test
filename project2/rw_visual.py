import matplotlib.pyplot as plt

from project2.random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
# plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
