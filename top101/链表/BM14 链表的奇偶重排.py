class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        odd = ListNode(-1)
        even = ListNode(-1)
        cnt = 0
        cur = head
        po = odd
        pe = even
        while cur:
            cnt += 1
            if cnt % 2 == 1:
                nxt = cur.next
                po.next = cur
                po = cur
                cur = nxt
            else:
                nxt = cur.next
                pe.next = cur
                pe = cur
                cur = nxt
        pe.next = None
        po.next = even.next

        return odd.next
