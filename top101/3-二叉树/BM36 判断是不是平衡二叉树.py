from reprlib import aRepr


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_balanced(root: TreeNode):
    if not root:
        return 0
    l = is_balanced(root.left)
    if l == -1:
        return -1

    r = is_balanced(root.right)
    if r == -1:
        return -1

    if abs(l - r) > 1:
        return -1

    return 1 + max(l, r)


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return bool布尔型
#
class Solution:
    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        # write code here
        return is_balanced(pRoot) != -1
