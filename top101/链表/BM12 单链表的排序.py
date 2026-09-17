from pickletools import read_uint1


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge(pHead1,pHead2) -> ListNode:
    dummy = ListNode(-1)
    pre = dummy
    p1=pHead1
    p2=pHead2
    while p1 and p2:
        if p1.val<=p2.val:
            nxt=p1.next
            pre.next=p1
            pre=p1
            p1=nxt
        else:
            nxt=p2.next
            pre.next=p2
            pre=p2
            p2=nxt
    if p1:
        pre.next=p1
    if p2:
        pre.next=p2

    return dummy.next

def sortList(head):
    if not head or not head.next:
        return head
    # 快慢指针找中点
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    l=sortList(head)
    r=sortList(mid)
    return merge(l,r)

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head node
# @return ListNode类
#
class Solution:
    def sortInList(self , head: ListNode) -> ListNode:
        # write code here
        return sortList(head)

