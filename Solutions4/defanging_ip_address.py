import re


class Solution:
    @staticmethod
    def defang_ip_address(address: str) -> str:
        defanged_ip = re.sub('\.', '[.]', address)
        return defanged_ip


ip = "1.1.1.1"
s = Solution()
print(s.defang_ip_address(ip))
