class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self, head: ListNode) -> bool:
        # write code here
        if not head or not head.next:
            return True
        l = 0
        p = head
        while p:
            l += 1
            p = p.next

        mid = l // 2
        p = head
        for _ in range(mid - 1):
            p = p.next

        if l % 2 == 1:
            p2 = p.next.next
        else:
            p2 = p.next
        p.next = None

        cur = head
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        p1 = pre
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
