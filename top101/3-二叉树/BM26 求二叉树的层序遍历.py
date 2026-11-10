class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型二维数组
#
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # write code here
        if not root:
            return []
        ans = []
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            # 一层一层统计
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(level)

        return ans
