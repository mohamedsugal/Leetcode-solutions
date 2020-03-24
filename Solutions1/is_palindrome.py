string = "A man, a plan, a canal"

def is_palindrome(string): 
    left = 0
    right = len(string) - 1

    while left < right: 
        if not string[left].isalnum(): 
            left += 1
        elif not string[right].isalnum(): 
            right -= 1
        else:  
            if string[left].lower() != string[right].lower(): 
                return False  
            left += 1
            right -= 1 

    return True

print(is_palindrome(string))