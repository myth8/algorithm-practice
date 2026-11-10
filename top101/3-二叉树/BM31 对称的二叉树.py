class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return bool布尔型
#
class Solution:
    def isMirror(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

    def isSymmetrical(self, pRoot: TreeNode) -> bool:
        # write code here
        if not pRoot:
            return True
        return self.isMirror(pRoot.left, pRoot.right)
