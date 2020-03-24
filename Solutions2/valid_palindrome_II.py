def validPalindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return isPalindrome(string, left + 1, right) or \
                   isPalindrome(string, left, right - 1)
        left += 1
        right -= 1
    return True

def isPalindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

test = "abc"
print(validPalindrome(test))
