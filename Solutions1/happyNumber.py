def isHappy(n): 
    # seen_nums = []

    # while n != 1: 
    #     if n in seen_nums: 
    #         return False 
    #     seen_nums.append(n)
    #     n = sum([int(i)**2 for i in str(n)])
    
    # return True
    seen = [] # our memoization
    while n not in seen:
        tmp = n 
        summ = 0 
        pop = 0
        while tmp > 0:
            pop = tmp % 10
            tmp = tmp // 10
            summ += pop ** 2
            
        if summ == 1:
            break
        
        seen.append(n)
        n = summ    
        
    return summ == 1

print(isHappy(19))