class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row = len(matrix)
        col = len(matrix[0])

        visited = [[False] * col for _ in range(row)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        r, c = 0, 0  # initialise top left coordinate
        d = 0

        res = []

        for _ in range(row * col):
            res.append(matrix[r][c])
            visited[r][c] = True

            dr, dc = directions[d]
            nr, nc = r + dr, c + dc

            if 0 <= nr < row and 0 <= nc < col and visited[nr][nc] is False:
                r, c = nr, nc
            else:
                d = (d + 1) % 4
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc
                r, c = nr, nc
        return res


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution().spiralOrder(matrix))
