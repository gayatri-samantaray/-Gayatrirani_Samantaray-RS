N = int(input("Enter how many numbers you want to sum: "))
sum_total = 0  
i = 1  

while i <= N:
    number = int(input(f"Enter number {i}: ")) 
    sum_total += number  
    i += 1  

print("Total Sum:", sum_total)