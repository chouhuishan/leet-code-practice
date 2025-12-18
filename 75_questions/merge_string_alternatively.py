# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)

        res = ""
        i = 0

        while i < w1 or i < w2:
            if i < w1:
                res += word1[i]
            if i < w2:
                res += word2[i]

            i += 1

        return res


# Time complexity = O(max(w1, w2))
# Space complexity = O(max(w1 + w2))


# word1 = "abc"
# word2 = "pqr"
# word1 = "ab"
# word2 = "pqrs"
word1 = "abcd"
word2 = "pq"
print(Solution().mergeAlternately(word1, word2))
