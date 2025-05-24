n = int(input("Enter a natural number: "))
for i in range(1, n + 1):
    sum_sq = 0  
    for j in range(1, i + 1):
        sum_sq += j * j 
    print(f"Sum of squares of first {i} numbers: {sum_sq}")