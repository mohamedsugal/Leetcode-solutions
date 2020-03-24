def longestPalindrome(s: str) -> str:
    dic = {}
    longest_substring = ""
    start = 0

    for end in range(len(s)): 
        char = s[end]
        if char in dic: 
            start = max(dic.get(char) + 1, start)
        if len(longest_substring) < end - start + 1: 
            longest_substring = s[start:end + 1]
        
        dic[char] = end

    return longest_substring

s = "babad"
print(longestPalindrome(s))