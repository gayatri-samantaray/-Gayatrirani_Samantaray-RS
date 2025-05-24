s=("aaabbccc")
def encode_string(s):
    result = ""
    i=0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1 
        if count >= 3:
            result += s[i] + str(count)
        else:
            result += s[i] * count  
        i+=1
        return result
    print(encode_string(s))