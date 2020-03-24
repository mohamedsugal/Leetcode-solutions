def count_and_say(n): 
    result = "1"
    for i in range(1, n): 
        temp = []
        counter = 1
        for j in range(1, len(result)): 
            if result[j] == result[j-1]: 
                counter += 1
            else: 
                temp.append(str(counter))
                temp.append(result[j-1])
                counter = 1
        temp.append(str(counter))
        temp.append(result[-1])
        result = ''.join(temp)
    return result 

print(count_and_say(4))

