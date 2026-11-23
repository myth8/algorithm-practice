#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 判断岛屿数量
# @param grid char字符型二维数组
# @return int整型
#
class Solution:
    def solve(self, grid: List[List[str]]) -> int:
        # write code here
        if not grid or not grid[0]:
            return 0
        cnt = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)

        return cnt
