class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_list(arrs):
    head = None
    for e in reversed(arrs):
        p = ListNode(e)
        p.next = head
        head = p
    return head

def display_list(head):
    p = head
    while p:
        print(p.val)
        p=p.next


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        cur = head
        pre = None
        while cur :
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre

if __name__ == "__main__":
    arrs = [1,2,3,4,5]
    head = create_list(arrs)
    sol = Solution()
    display_list(sol.ReverseList(head))
