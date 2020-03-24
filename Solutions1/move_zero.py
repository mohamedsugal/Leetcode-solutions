def move_zero(arr): 
    index = 0 
    for i in range(len(arr)): 
        if arr[i] != 0: 
            temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp 
            index += 1
    return arr 


arr = [0,1,0,3,12]
print(move_zero)