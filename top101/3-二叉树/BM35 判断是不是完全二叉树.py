import queue


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
    def isCompleteTree(self , root: TreeNode) -> bool:
        # write code here
        from collections import deque
        q = deque()
        if not root:
            return True
        q.append(root)
        flag = False
        while len(q)!=0:
            cur = q.popleft()
            if flag:
                if cur.left or cur.right:
                    return False
                continue
            if not cur.left and cur.right:
                return False
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if not cur.left or not cur.right:
                flag = True

        return True
