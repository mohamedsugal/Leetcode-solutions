import unittest
import logging

class Solution:
    def decodeString(self, decodedString: str) -> str:
        stack = [[[], 1]]
        digit = 0
        for letter in decodedString: 
            if letter.isdigit():
                digit = digit * 10 + ord(letter) - ord('0')
            elif letter == "[":
                stack.append([[], digit])
                digit = 0
            elif letter == "]": 
                ch, n = stack.pop()
                stack[-1][0].extend(ch * n)
            else: 
                stack[0][0].append(letter)
        return "".join(stack[0][0])

class TestSolution(unittest.TestCase):     
    def test1(self): 
        self.assertEqual(Solution().decodeString("3[a2[c]]"), "accaccacc")
    def test2(self): 
        self.assertEqual(Solution().decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
    def test3(self): 
        self.assertEqual(Solution().decodeString("abc3[cd]xyz"), "abccdcdcdxyz")

if __name__ == "__main__":
    unittest.main()