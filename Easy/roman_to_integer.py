class Solution:
    def romanToInt(self, s: str) -> int:
        symbols_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        previous_v = 0

        for char in s[::-1]:
            current_v = symbols_dict[char]
            if current_v < previous_v:
                total -= current_v

            else:
                total += current_v
                previous_v = current_v
        return total


# s = "III"
# s = "LVIII"
s = "MCMXCIV"
print(Solution().romanToInt(s))
