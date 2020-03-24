nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
    # Time Complexity: O(n)
    # Space Complexity: O(n) because of use of another Array
    rotated_array = [0] * len(nums)
    for i in range(len(nums)): 
        rotated_array[i] = nums[(i - k) % len(nums)]
    return rotated_array 

print(rotate(nums, k))

def rotate_array(nums, k): 
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums

def reverse(nums, start, end): 
    while start < end: 
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp 
        start += 1
        end -= 1

print(rotate_array(nums, k))