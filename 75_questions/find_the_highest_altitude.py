class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = []
        current_sum = 0
        altitude.append(current_sum)

        for i in gain:
            current_sum += i
            altitude.append(current_sum)
            i += 1
        return max(altitude)


# gain = [-5, 1, 5, 0, -7]
gain = [-4, -3, -2, -1, 4, 3, 2]
print(Solution().largestAltitude(gain))
