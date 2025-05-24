import numpy as np
identity_matrix = np.eye(5)
identity_matrix[np.eye(5, dtype=bool)] = np.arange(1, 6)
print("Modified Identity Matrix:\n", identity_matrix)