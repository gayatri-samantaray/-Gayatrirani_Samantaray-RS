my_list = ['a', 'b', 'c']
my_dict = {'a': 100, 'c': 200, 'd': 300}
K = 'c'  
if K in my_list and K in my_dict:
    print(f"Value of '{K}' from dictionary:", my_dict[K])
else:
    print(f"Key '{K}' not present in both list and dictionary.")