def longestSubstring(string): 
    dictionary = {}
    longest_substring = ""
    start = 0 
    
    for end in range(len(string)): 
        char = string[end] 
        if char in dictionary: 
            start = max(dictionary.get(char)+1, start)
        if len(longest_substring) < end - start + 1: 
            longest_substring = string[start:end+1]
        
        dictionary[char] = end
    
    return longest_substring

string = "pwwke"
print(longestSubstring(string))