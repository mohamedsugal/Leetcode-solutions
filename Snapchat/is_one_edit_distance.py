import unittest

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t: 
            return False 
        if len(t) > len(s): 
            self.isOneEditDistance(t, s)
        i = j = edit = 0 
        while i < len(s) and j < len(t): 
            if s[i] != t[j]: 
                edit += 1
                if len(s) > len(t): 
                    i += 1
                else: 
                    i += 1; j += 1
            else: 
                i += 1; j += 1
            if edit > 1: 
                return False 
        return True

class Test_isOneEditDistance(unittest.TestCase):     
    def test_s_greater_than_t(self): 
        self.assertTrue(Solution().isOneEditDistance("abc", "ab"))
    def test_t_greater_than_s(self):
        self.assertTrue(Solution().isOneEditDistance("ab", "acb"))
    def test_equal_string(self): 
        self.assertFalse(Solution().isOneEditDistance("c", "c"))


if __name__ == '__main__':
    unittest.main()