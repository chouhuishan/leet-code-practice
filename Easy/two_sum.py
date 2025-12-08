# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]
#         return []


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hashtable:
                return [idx, hashtable.get(complement)]
            hashtable[num] = idx


# nums = [2, 7, 11, 15]
# target = 9
# nums = [3, 2, 4]
# target = 6
nums = [3, 3]
target = 6
print(Solution().twoSum(nums, target))
