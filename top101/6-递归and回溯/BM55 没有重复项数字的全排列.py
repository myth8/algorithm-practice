#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def permute(self, num: List[int]) -> List[List[int]]:
        # write code here
        n = len(num)
        path = []
        used = [False] * n
        ans = []

        def dfs():
            if len(path) == n:
                ans.append(path.copy())
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(num[i])
                    dfs()
                    path.pop()
                    used[i] = False

        dfs()
        return ans
