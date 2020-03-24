def reverseWords(string: str) -> str:
    words = " ".join(string.split())
    words = [word for word in words.split(' ')]
    
    left, right = 0, len(words) - 1
    while left < right: 
        temp = words[left]
        words[left] = words[right]
        words[right] = temp
        left += 1
        right -= 1
    
    return ' '.join(words)
    


string = "   Hello    World!    "
print(reverseWords(string))