class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []

        max_candies = max(candies)

        for candy in candies:
            total = candy + extraCandies
            if total >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res


candies = [2, 3, 5, 1, 3]
extraCandies = 3
# candies = [4, 2, 1, 1, 2]
# extraCandies = 1
# candies = [12, 1, 12]
# extraCandies = 10
print(Solution().kidsWithCandies(candies, extraCandies))
