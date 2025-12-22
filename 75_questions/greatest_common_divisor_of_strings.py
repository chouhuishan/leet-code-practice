# For two strings s and t, we say "t divides s"
# if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]


# m = len(str1)
# 2 = len(str2)

# Time complexity : O(m + n)
# Space complexity : O(m + n)

str1 = "ABCABC"
str2 = "ABC"
# str1 = "ABABAB"
# str2 = "ABAB"
# str1 = "LEET"
# str2 = "CODE"
# str1 = "AAAAAB"
# str2 = "AAA"
print(Solution().gcdOfStrings(str1, str2))
