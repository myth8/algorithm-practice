class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 求二叉树的右视图
# @param preOrder int整型一维数组 先序遍历
# @param inOrder int整型一维数组 中序遍历
# @return int整型一维数组
#
class Solution:
    def solve(self, preOrder: List[int], inOrder: List[int]) -> List[int]:
        # write code here
        pos = {v: i for i, v in enumerate(inOrder)}

        def build(preL, preR, inL, inR):
            if preL > preR: return None
            val = preOrder[preL]
            root = TreeNode(val)
            idx = pos[val]
            leftTreeSize = idx - inL
            root.left = build(preL + 1, preL + leftTreeSize, inL, idx - 1)
            root.right = build(preL + leftTreeSize + 1, preR, idx + 1, inR)
            return root

        root = build(0, len(preOrder) - 1, 0, len(inOrder) - 1)
        from collections import deque
        q = deque()
        q.append(root)
        ans = []
        while q:
            n = len(q)
            for i in range(n):
                r = q.popleft()
                if i == n-1:
                    ans.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)

        return ans
