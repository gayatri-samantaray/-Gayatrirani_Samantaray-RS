
def find_missing_number(lst):
n = len(lst)+1
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
missing = expected_sum - actual_sum
return missing
numbers = [1, 2, 4, 5]
print("Missing number is:",find_missing_number(numbers)) 