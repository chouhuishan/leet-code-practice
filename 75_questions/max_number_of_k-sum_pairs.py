# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        total_ops = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == k:
                total_ops += 1
                left += 1
                right -= 1

            elif nums[left] + nums[right] > k:
                right -= 1

            else:
                left += 1

        return total_ops


nums = [1, 2, 3, 4]
k = 5
nums = [3, 1, 3, 4, 3]
k = 6
print(Solution().maxOperations(nums, k))
