class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        ansNode = ListNode(-1)
        pre = ansNode
        p1d = ListNode(-1)
        p1d.next = pHead1
        p2d = ListNode(-1)
        p2d.next = pHead2
        p1 = pHead1
        p1f = p1d
        p2 = pHead2
        p2f = p2d
        while p1 and p2:
            if p1.val <= p2.val:
                p = p1
                p1 = p1.next
                pre.next = p
                pre = p
            else:
                p = p2
                p2 = p2.next
                pre.next = p
                pre = p

        while p1:
            p = p1
            p1 = p1.next
            pre.next = p
            pre = p
        while p2:
            p = p2
            p2 = p2.next
            pre.next = p
            pre = p

        pre.next = None
        return ansNode.next
            
