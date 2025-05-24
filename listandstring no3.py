lst = [('a', 1), ('b', 2), ('a', 3)]
b = {}

for key, value in lst:
    if key not in b:
        b[key] = []
    b[key].append(value)
print(b)  
