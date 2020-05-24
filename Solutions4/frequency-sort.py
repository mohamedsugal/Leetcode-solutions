from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        vals = list(count.items())
        vals.sort(key=lambda x: x[1], reverse=True)

        res = ""
        for char, freq in vals:
            res += char * freq
        return res


s = "Aabb"
solution = Solution()
print(solution.frequencySort(s))
