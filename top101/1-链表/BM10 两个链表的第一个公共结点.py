# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        l1 = 0
        l2 = 0
        p1 = pHead1
        p2 = pHead2
        while p1:
            l1 += 1
            p1 = p1.next
        while p2:
            l2 += 1
            p2 = p2.next

        k = abs(l1 - l2)
        h1 = pHead1
        h2 = pHead2
        if l1 > l2:
            for _ in range(k):
                h1 = h1.next
        if l2 > l1:
            for _ in range(k):
                h2 = h2.next

        while h1 and h2:
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next

        return None
