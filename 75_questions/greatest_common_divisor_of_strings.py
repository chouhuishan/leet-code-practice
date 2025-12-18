from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]


str1 = "ABCABC"
str2 = "ABC"
# str1 = "ABABAB"
# str2 = "ABAB"
# str1 = "LEET"
# str2 = "CODE"
# str1 = "AAAAAB"
# str2 = "AAA"
print(Solution().gcdOfStrings(str1, str2))
