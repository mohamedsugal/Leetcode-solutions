from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        for word in strs:
            key = self.convert(word)
            if key in groupings:
                groupings[key].append(word)
            else:
                groupings[key] = [word]
        return [*groupings.values()]

    @staticmethod
    def convert(word):
        alphabet = [0] * 26
        for letter in word:
            alphabet[ord(letter) - ord('a')] += 1
        return tuple(alphabet)


values = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.group_anagrams(values))
