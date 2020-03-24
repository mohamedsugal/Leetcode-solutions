from typing import List 

def findShortestSubArray(nums: List[int]) -> int:
    min_length = 0
    degree = 0
    count = {}
    first_seen = {}
    
    for i, n in enumerate(nums): 
        if n not in first_seen: 
            first_seen[n] = i
        
        count[n] = count.get(n, 0) + 1
        if count[n] > degree: 
            degree = count[n]
            min_length = (i - first_seen[n]) + 1
        elif count[n] == degree: 
            min_length = min(min_length, (i - first_seen[n]) + 1)

    print(first_seen)
    print(count)
    return min_length


# nums = [1,2,2,3,1,4,2]
# nums = [1, 2, 2, 3, 1]
nums = [2,1,1,2,1,3,3,3,1,3,1,3,2]
print(findShortestSubArray(nums))