# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

# Note that the integers in the lists may be returned in any order.


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # not_in_1 = set()
        # not_in_2 = set()

        # for i in nums1:
        #     if i not in nums2:
        #         not_in_2.add(i)

        # for j in nums2:
        #     if j not in nums1:
        #         not_in_1.add(j)

        # not_in_2_list = list(not_in_2)
        # not_in_1_list = list(not_in_1)

        # return [not_in_2_list, not_in_1_list]

        # nums1 = set(nums1)
        # nums2 = set(nums2)

        # not_in_2 = nums1 - nums2
        # not_in_1 = nums2 - nums1

        # return [list(not_in_2), list(not_in_1)]

        nums1 = set(nums1)
        nums2 = set(nums2)

        distinct_in_nums1 = nums1.difference(nums2)
        distinct_in_nums2 = nums2.difference(nums1)

        return [list(distinct_in_nums1), list(distinct_in_nums2)]


# Time complexity = O(n)
# Space complexity = O(n)


# nums1 = [1, 2, 3]
# nums2 = [2, 4, 6]
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
print(Solution().findDifference(nums1, nums2))
