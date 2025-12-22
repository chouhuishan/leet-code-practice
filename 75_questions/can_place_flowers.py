# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# and an integer n, return true if n new flowers can be planted in the flowerbed
# without violating the no-adjacent-flowers rule and false otherwise.


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # flower = 0

        # for i in range(len(flowerbed)):
        #     if flowerbed[i] == 0:
        #         is_left_empty = (i == 0) or (flowerbed[i - 1] == 0)
        #         is_right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

        #         if is_left_empty and is_right_empty:
        #             flowerbed[i] = 1
        #             flower += 1
        #             if flower >= n:
        #                 return True
        # return False

        flower = 0

        if n == 0:
            return True

        for idx, bed in enumerate(flowerbed):
            if bed == 0:
                is_left_empty = (idx == 0) or (flowerbed[idx - 1] == 0)
                is_right_empty = (idx == len(flowerbed) - 1) or (
                    flowerbed[idx + 1] == 0
                )

                if is_left_empty and is_right_empty:
                    flowerbed[idx] = 1
                    flower += 1
                    if flower == n:
                        return True
        return False


# n = len(flowerbed)

# Time complexity : O(n)
# Space complexity : O(1)

# flowerbed = [1, 0, 0, 0, 1]
# n = 1
flowerbed = [1, 0, 0, 0, 1]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))
