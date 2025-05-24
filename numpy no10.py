import numpy as np
arr = np.array([])
for num in [4, 5, 6]:
    if num % 2 == 0:
        arr = np.append(arr, num)
print("\nTask 10 - Appended Even Numbers:", arr)
