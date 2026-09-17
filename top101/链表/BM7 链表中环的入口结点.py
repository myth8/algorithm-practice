# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return None
        slow = pHead
        fast = pHead
        meet = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = slow
                break
        if not meet:
            return None
        # 从相遇点和头节点同时出发，找入环点
        head = pHead
        while head != meet:
            head = head.next
            meet = meet.next
            
        return head
