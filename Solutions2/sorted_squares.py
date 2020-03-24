from typing import List 

def sortedSquares(A: List[int]) -> List[int]:
    answer = [0] * len(A)
    l, r = 0, len(A) - 1

    while l <= r: 
        left, right = abs(A[l]), abs(A[r])
        if left > right: 
            answer[r - l] = left * left 
            l += 1
        else: 
            answer[r - l] = right * right 
            r -= 1
    return answer


A = [-7,-3,2,3,11]
print(sortedSquares(A))

