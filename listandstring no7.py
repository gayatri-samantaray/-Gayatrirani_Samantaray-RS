1st=(["abc","def",["ghi","jkl"]])
def flatten_chars(lst):
    result = []

    for item in lst:
        if isinstance(item, list):  
                result.extend(list(word)) 
            result.extend(list(item)) 

    return result


print(flatten_chars(["abc", "def", ["ghi", "jkl"]]))
