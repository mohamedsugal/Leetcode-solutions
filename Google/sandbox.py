# arr1 = [4, 6, 9, 3]
# arr2 = [8, 7, 5, 134]


arr1 = [10, 1000]
arr2 = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]


# arr1.sort()
def sorting(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


def smallestDifference(arrayOne, arrayTwo):
    closest = float('inf')
    for p1 in range(len(arrayOne)):
        for p2 in range(len(arrayTwo)):
            current = abs(arrayOne[p1] - arrayTwo[p2])
            closest = min(closest, current)

    for p1 in range(len(arrayOne)):
        for p2 in range(len(arrayTwo)):
            if abs(arrayOne[p1] - arrayTwo[p2]) == closest:
                return [arrayOne[p1], arrayTwo[p2]]
    return -1


print(smallestDifference(arr1, arr2))

# "arrayOne": [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123],
#   "arrayTwo": [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
