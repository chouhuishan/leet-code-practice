# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string
# by deleting some (can be none) of the characters without disturbing the
# relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1 = len(s)
        t1 = len(t)

        i = j = 0

        while i < s1 and j < t1:
            if s[i] == t[j]:
                i += 1
            #     j += 1
            # else:
            #     j += 1
            j += 1
        return True if i == s1 else False


s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
print(Solution().isSubsequence(s, t))
