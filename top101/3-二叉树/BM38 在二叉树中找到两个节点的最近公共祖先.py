class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, o1: int, o2: int) -> int:
        def dfs(root):
            if not root or root.val == o1 or root.val == o2:
                return root
            l = dfs(root.left)
            r = dfs(root.right)
            if l and r:
                return root
            if l and not r:
                return l
            if not l and r:
                return r

            return None

        res = dfs(root)
        return res.val if res else -1
