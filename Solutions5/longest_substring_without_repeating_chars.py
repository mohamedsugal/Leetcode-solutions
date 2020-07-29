class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        start, longest = 0, ""
        seen = {}
        for end, char in enumerate(s):
            if char in seen:
                start = max(start, seen[char]+1)
            if len(longest) < end - start + 1:
                longest = s[start:end+1]

            seen[char] = end
        return len(longest)


string = "pwwkew"
solution = Solution()
print(solution.length_of_longest_substring(string))


