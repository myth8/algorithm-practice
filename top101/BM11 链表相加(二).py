class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head: ListNode):
    if not head:
        return None
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    return pre

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#
class Solution:
    def addInList(self , head1: ListNode, head2: ListNode) -> ListNode:
        # write code here
        dummy_ans = ListNode(-1)
        pre = dummy_ans
        h1 = reverseList(head1)
        h2 = reverseList(head2)
        add = 0
        while h1 or h2 or add:
            s = add
            if h1:
                s+=h1.val
                h1=h1.next
            if h2:
                s+=h2.val
                h2=h2.next
            cur=ListNode(s%10)
            add=s//10
            pre.next=cur
            pre=cur

        pre.next = None

        return reverseList(dummy_ans.next)
