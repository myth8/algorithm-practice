#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return string字符串一维数组
#
class Solution:
    def Permutation(self, str: str) -> List[str]:
        # write code here
        if not str:
            return []
        ans = []
        n = len(str)
        s = sorted(str)
        path = []
        used = [False] * n

        def dfs():
            if len(path) == n:
                ans.append(''.join(path))
                return

            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(s[i])
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return ans
