class Solution:
    @staticmethod
    def reverse_words(s: str) -> str:
        pass


def test_solution():
    test = Solution()
    assert test.reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert test.reverse_words("It is cool") == "tI si looc"
