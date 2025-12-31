# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        initial_sum = sum(nums[:k])
        max_sum = initial_sum

        for i in range(n - k):
            next_sum = initial_sum - nums[i] + nums[k - i]
            max_sum = max(max_sum, next_sum)
        return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(Solution().findMaxAverage(nums, k))
