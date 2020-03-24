def two_sum(nums, target): 
    number_seen = {}
    for i in range(len(nums)): 
        if nums[i] in number_seen: 
            return [number_seen[nums[i]], i]
        else: 
            number_seen[target-nums[i]] = i

def brute_force_two_sum(nums, target): 
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)): 
            if nums[i] + nums[j] == target: 
                return [i, j]

def two_sum_pointers(nums, target): 
    nums.sort()
    left = 0
    right = len(nums)-1
    while left < right: 
        curr_sum = nums[left] + nums[right]
        if curr_sum == target: 
            return [left, right]
        elif curr_sum < target: 
            left += 1
        else: 
            right -= 1

       
nums = [11, 4, 7, 2]
target = 9
print(two_sum(nums, target))
print(brute_force_two_sum(nums, target))
print(two_sum_pointers(nums, target))