class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder(root, ans):
    if not root:
        return
    inorder(root.left, ans)
    ans.append(root.val)
    inorder(root.right, ans)


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # write code here
        ans = []
        inorder(root, ans)
        return ans
