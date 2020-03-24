def reverse_string(string): 
    left = 0 
    right = len(string)-1
    while left < right: 
        temp = string[left]
        string[left] = string[right]
        string[right] = temp 
        left += 1
        right -= 1
    return string 

string = ['h', 'e', 'l', 'l', 'o']
print(reverse_string(string))