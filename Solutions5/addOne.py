from typing import List


def add_one(arr: List[int]) -> List[int]:
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 9:
            arr[i] = 0
        else:
            arr[i] += 1
            return arr
    return [1] + arr


num = [2, 9, 9]
print(add_one(num))

