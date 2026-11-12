class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param preOrder int整型一维数组
# @param vinOrder int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self, preOrder: List[int], vinOrder: List[int]) -> TreeNode:
        # write code here
        pos = {v: i for i, v in enumerate(vinOrder)}

        def build(preL, preR, inL, inR):
            if preL > preR: return None
            val = preOrder[preL]
            root = TreeNode(val)
            idx = pos[val]
            leftTreeSize = idx - inL
            root.left = build(preL + 1, preL + leftTreeSize, inL, idx - 1)
            root.right = build(preL + leftTreeSize + 1, preR, idx + 1, inR)
            return root

        return build(0, len(preOrder) - 1, 0, len(vinOrder) - 1)
