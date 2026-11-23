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
        from collections import deque
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    grid[i][j] = '0'
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            xl, yl = x + dx, y + dy
                            if 0 <= xl < m and 0 <= yl < n and grid[xl][yl] == '1':
                                grid[xl][yl] = '0'
                                q.append((xl, yl))
        return cnt
