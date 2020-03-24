def validAnagram(s1, s2):
    if s1 is None or s2 is None: 
        return False 
    if len(s1) != len(s2): 
        return False 
    
    dic = {}
    for c in s1: 
        dic[c] = dic.get(c, 0) + 1
    for c in s2: 
        if dic.get(c, 0) < 1: 
            return False
        dic[c] = dic.get(c, 0) - 1
    return True

validAnagram("abc", "cat")
    