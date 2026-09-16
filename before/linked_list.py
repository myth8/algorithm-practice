"""单链表的创建、反转与测试（Python3）"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def create_list(values):
    """根据序列创建单链表，返回头节点。空序列返回 None。"""
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    """链表转 Python 列表，便于断言/打印。"""
    result = []
    node = head
    while node:
        result.append(node.val)
        node = node.next
    return result


def reverse_list(head):
    """迭代法原地反转链表，返回新头节点。"""
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse_list_recursive(head):
    """递归法反转链表。"""
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [7],
        [],
        [3, 3, 3],
    ]

    for values in test_cases:
        head = create_list(values)
        print(f"原始链表: {to_list(head)}")
        print(f"迭代反转: {to_list(reverse_list(head))}")
        head2 = create_list(values)
        print(f"递归反转: {to_list(reverse_list_recursive(head2))}")
        print("-" * 20)
