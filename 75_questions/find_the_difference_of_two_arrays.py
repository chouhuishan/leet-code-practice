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

        nums1 = set(nums1)
        nums2 = set(nums2)

        not_in_2 = nums1 - nums2
        not_in_1 = nums2 - nums1

        return [list(not_in_2), list(not_in_1)]


# Time complexity = O(n)
# Space complexity = O(n)


# nums1 = [1, 2, 3]
# nums2 = [2, 4, 6]
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
print(Solution().findDifference(nums1, nums2))
