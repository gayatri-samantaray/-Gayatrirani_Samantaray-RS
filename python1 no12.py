data = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)
columns = zip(*data)
averages = [sum(col) / len(col) for col in columns]
print("Column-wise averages:", averages)