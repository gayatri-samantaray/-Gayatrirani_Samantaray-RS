import numpy as np
array = np.random.randint(1, 100, (5, 5))
border = np.concatenate([array[0], array[-1], array[1:-1, 0], array[1:-1, -1]])
print("Original Array:\n", array)
print("Border Elements:\n", border)