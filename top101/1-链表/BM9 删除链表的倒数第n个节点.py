class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param n int整型
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self , head: ListNode, n: int) -> ListNode:
        # write code here
        slow = head
        fast = head
        for _ in range(n):
            if not fast:
                return None
            fast = fast.next

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while fast:
            pre = slow
            slow = slow.next
            fast = fast.next

        pre.next = slow.next

        return dummy.next