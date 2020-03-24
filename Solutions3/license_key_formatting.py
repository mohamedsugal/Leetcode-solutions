class Solution:
    @staticmethod
    def license_key_formatting(plate: str, k: int) -> str:
        plate = plate.upper().replace("-", "")
        index = k if len(plate) % k == 0 else len(plate) % k
        res = plate[:index]
        while index < len(plate):
            res += "-" + plate[index:index+k]
            index += k
        return res


# plate_num = "5F3Z-2e-9-w"
# val = 4
plate_num = "a-a-a-a-"
val = 1
t = Solution()
print(t.license_key_formatting(plate_num, val))
