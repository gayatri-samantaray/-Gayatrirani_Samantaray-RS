def is_power_of_2(n):
   if n <= 0:
       return False
while n % 2 == 0:
        n = n // 2
return n == 1
number = int(input("Enter a number: "))
print("Is power of 2:", is_power_of_2(number))