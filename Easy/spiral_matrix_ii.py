class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[False] * n for _ in range(n)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = 0, 0  # initialise top left coordinates
        d = 0

        for num in range(1, n * n + 1):
            matrix[r][c] = num

            dr, dc = directions[d]
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] is False:
                matrix[nr][nc] = num
            else:
                d = (d + 1) % 4
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc

            r, c = nr, nc

        return matrix


n = 3
# n = 1
print(Solution().generateMatrix(n))
