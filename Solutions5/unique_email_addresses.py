from typing import List


class Solution:
    @staticmethod
    def num_unique_emails(emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split("@")
            if "+" in local:
                local = local[:local.index("+")]
            seen.add(local.replace(".", "") + "@" + domain)
        return len(seen)


mails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
solution = Solution()
print(solution.num_unique_emails(mails))