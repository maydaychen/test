import json
from numpy import *;
from matplotlib import *;

numbers = [1, 3, 5, 7, 9]
filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
