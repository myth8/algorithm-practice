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
# @param k int整型 
# @return ListNode类
#
class Solution:
    def reverseKGroup(self , head: ListNode, k: int) -> ListNode:
        # write code here
        l = 0
        p = head
        while p:
            l+=1
            p = p.next

        i = 1
        dummy = ListNode(-1)
        dummy.next = head
        pf = dummy
        cur = head
        while i + k - 1 <= l:
            pm = cur
            j = i
            pn = pm
            while j < i + k -1:
                pn = pn.next
                j+=1
            ns = pn.next

            now = pm
            pre = ns
            while now != ns:
                nxt = now.next
                now.next = pre
                pre = now
                now = nxt

            pf.next = pre
            pf = pm
            cur = ns
            i = j + 1

        return dummy.next

if __name__ == "__main__":
    arrs = [1,2,3,4,5]
    head = create_list(arrs)
    sol = Solution()
    display_list(sol.reverseKGroup(head,2))
