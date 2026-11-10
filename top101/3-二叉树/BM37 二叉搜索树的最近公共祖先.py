class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        # write code here
        while root:
            if p < root.val and q < root.val:
                root = root.left
            elif p > root.val and q > root.val:
                root = root.right
            else:
                return root.val
        return None
