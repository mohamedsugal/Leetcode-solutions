def isBadVersion(version):
    return False



def firstBadVersion(n):
    return firstBadVersionRecursion(1, n)

def firstBadVersionRecursion(left, right): 
    if left > right: 
        return left 
    mid = (left + right) // 2
    if isBadVersion(mid): 
        return firstBadVersionRecursion(left, mid - 1)
    else: 
        return firstBadVersionRecursion(right + 1, mid)

def firstBadVersionIter(n): 
    left, right = 1, n 
    while left < right: 
        mid = (left + right) // 2
        if isBadVersion(mid) == False: 
            left = mid + 1 
        else: 
            right = mid 
    
    return left 


print(firstBadVersion(34))
print(isBadVersion(25))