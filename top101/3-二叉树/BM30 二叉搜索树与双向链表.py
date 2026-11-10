class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param pRootOfTree TreeNode类
# @return TreeNode类
#
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        # pre 记录中序遍历中上一个访问的节点
        # 用 self.pre 而不是全局变量，避免多次调用污染
        self.pre = None

        def inOrder(root: TreeNode):
            if not root:
                return
            inOrder(root.left)
            if self.pre:
                self.pre.right = root
            root.left = self.pre
            self.pre = root
            inOrder(root.right)

        inOrder(pRootOfTree)
        p = pRootOfTree
        while p.left:
            p = p.left
        return p
