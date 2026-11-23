#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def permuteUnique(self, num: List[int]) -> List[List[int]]:
        # write code here
        n = len(num)
        num.sort()
        path = []
        used = [False] * n
        ans = []

        def dfs():
            if len(path) == n:
                ans.append(path.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and num[i] == num[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(num[i])
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return ans
