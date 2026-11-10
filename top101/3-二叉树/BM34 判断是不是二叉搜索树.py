class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return bool布尔型
#
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # write code here
        if not root:
            return True
        self.pre = None

        def isBst(root: TreeNode) -> bool:
            if not root:
                return True
            if not isBst(root.left):
                return False
            if self.pre:
                if self.pre.val >= root.val:
                    return False
            self.pre = root
            return isBst(root.right)

        return isBst(root)
