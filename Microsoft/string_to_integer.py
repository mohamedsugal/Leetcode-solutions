def atoi(string: str) -> int:
    s = list(string.strip())
    print(s)
    if len(string) == 0 or not s:
        return 0
    sign = -1 if s[0] == "-" else 1
    if s[0] in "+-":
        del s[0]
    res = i = 0
    while i < len(s) and s[i].isdigit():
        res = 10 * res + (ord(s[i]) - ord('0'))
        i += 1
    return max(-2 ** 31, min(res * sign, 2 ** 31))


string = "   00420"
string2 = "word 096"
string3 = " "
print(atoi(string3))
