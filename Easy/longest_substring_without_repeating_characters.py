class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashtable = {}  # char to the latest index
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in hashtable and hashtable[char] >= left:
                left = hashtable[char] + 1

            hashtable[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len


# s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
