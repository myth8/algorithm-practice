# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param m int整型 
# @param n int整型 
# @return ListNode类
#
class Solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        dummy = ListNode(-1)
        dummy.next = head
        pf = dummy
        p = head
        cnt = 0
        while p:
            cnt+=1
            if cnt == m:
                pm = p
                mf = pf
            if cnt == n:
                ns = p.next
            pf = p
            p = p.next

        cur = pm
        pre = ns
        while cur != ns:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        mf.next = pre

        return dummy.next
