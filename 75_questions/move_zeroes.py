# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # i = 0

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.remove(0)
        #         nums.append(0)
        #         i += 1
        #     i += 1
        # return nums

        i = 0

        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
                i += 1
            i += 1
        return nums


# Time complexity = O(n**2)
# Space complexity = O(1)


nums = [0, 1, 0, 3, 12]
# nums = [0]
print(Solution().moveZeroes(nums))
