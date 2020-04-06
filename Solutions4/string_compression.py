from typing import List

# Naive solution 
def string_compression(text): 
    count = 0
    result = []
    for i in range(len(text)): 
        count += 1
        if i + 1 >= len(text) or text[i] != text[i+1]: 
            result.append(text[i])
            if count > 1: 
                result.append(str(count))
            count = 0
    return "".join(result)

class Solution:
    @staticmethod
    def compress(chars: List[str]) -> int:
        res = []
        count, index = 1, 0
        for curr in range(1, len(chars)+1):
            prev = curr - 1
            if curr < len(chars) and chars[prev] == chars[curr]:
                count += 1
            else:
                chars[index] = chars[prev]
                index += 1
                if count > 1:
                    for n in str(count):
                        chars[index] = n
                        index += 1
                count = 1
        chars = chars[:index]
        print(chars)
        return index


string = ["a", "a", "b", "b", "c", "c", "c"]
solution = Solution()
print(solution.compress(string))
