# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and s[left].lower() not in vowels:
                left += 1
            while left < right and s[right].lower() not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


# Time complexity = O(n)
# Space complexity = O(n)


# s = "IceCreAm"
s = "leetcode"
print(Solution().reverseVowels(s))
