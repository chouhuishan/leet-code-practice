<<<<<<< HEAD
=======
# Given an array of integers arr, return true if the number of occurrences
# of each value in the array is unique or false otherwise.

>>>>>>> 7859a2f (lc leaf similar trees solve)
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = Counter(arr)
        unique_counts = set(counts.values())

        if len(counts) != len(unique_counts):
            return False
        else:
            return True


# arr = [1, 2, 2, 1, 1, 3]
# arr = [1, 2]
arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
print(Solution().uniqueOccurrences(arr))
