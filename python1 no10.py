list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 5]
set1 = set(list1)
set2 = set(list2)
missing = set1.symmetric_difference(set2)

print("Missing element:", missing)