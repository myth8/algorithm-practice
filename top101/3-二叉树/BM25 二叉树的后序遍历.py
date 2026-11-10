class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postorder(root, ans):
    if not root:
        return
    postorder(root.left, ans)
    postorder(root.right, ans)
    ans.append(root.val)


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # write code here
        ans = []
        postorder(root, ans)
        return ans
