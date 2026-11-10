class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return int整型二维数组
#
class Solution:
    def Print(self, pRoot: TreeNode) -> List[List[int]]:
        # write code here
        if not pRoot:
            return []
        from collections import deque
        q = deque()
        q.append(pRoot)
        is_right = False
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if is_right:
                level.reverse()
            ans.append(level)
            is_right = not is_right

        return ans
