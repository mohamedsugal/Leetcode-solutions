from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    seen, count = set(), {}
    
    for n in nums1: 
        count[n] = count.get(n, 0) + 1
    
    for n in nums2: 
        if n in count: 
            seen.add(n)
    
    return list(seen)


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))