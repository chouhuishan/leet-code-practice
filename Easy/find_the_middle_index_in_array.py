class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1


# nums = [2, 3, -1, 8, 4]
# nums = [1, -1, 4]
nums = [2, 5]
print(Solution().findMiddleIndex(nums))
