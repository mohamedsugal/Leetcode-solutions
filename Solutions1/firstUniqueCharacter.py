def first_unique_char(string): 
    count = {}
    for i in string:
        count[i] = count.get(i, 0)+1
    
    for i in range(len(string)): 
        if count[string[i]] == 1: 
            return i
    
    # for index, char in enumerate(string): 
    #     if count[char] == 1: 
    #         return index 
    return -1 

string = "loetcleetcvode"
print(first_unique_char(string))
