#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return string字符串一维数组
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # write code here
        ans = []

        def dfs(path, left, right):
            if left == n and right == n:
                ans.append(''.join(path))
                return

            if left < n:
                path.append('(')
                dfs(path, left + 1, right)
                path.pop()

            if right < left:
                path.append(')')
                dfs(path, left, right + 1)
                path.pop()

        dfs([], 0, 0)
        return ans
