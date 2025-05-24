import numpy as np
a = np.array([[1,2], [3,4], [1,2]])
unique_rows = np.unique(a, axis=0)
print("Unique Rows:\n", unique_rows)