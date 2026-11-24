#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 递增路径的最大长度
# @param matrix int整型二维数组 描述矩阵的每个数
# @return int整型
#
class Solution:
    def solve(self, matrix: List[List[int]]) -> int:
        # write code here
        from functools import cache
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def dfs(i, j):
            max_len = 1

            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(x, y))

            return max_len

        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans
