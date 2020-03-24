def max_subarray(nums):
    # kadane algorithm 
    max_so_far = max_ending = 0     
    begin = start = end = 0 

    for i in range(len(nums)):
        max_ending += nums[i]
        if max_ending < 0: 
            max_ending = 0
            begin = i + 1 

        if max_so_far < max_ending: 
            max_so_far = max_ending
            start = begin
            end = i 
    
    return nums[start:end+1]

def maxSubArray(nums): 
    #Greedy Algorith
    curr_sum = max_sum = nums[0]
    for i in nums[1:]: 
        curr_sum = max(i, curr_sum + i)
        max_sum = max(max_sum, curr_sum)
    return max_sum

    

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
print(maxSubArray(nums))
