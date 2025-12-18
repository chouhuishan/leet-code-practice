# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        stack = []

        current_node = head

        while current_node.next is not None:
            stack.append(current_node)
            current_node = current_node.next

        head = current_node

        while stack:
            head.next = stack.pop()
            head = head.next

        head.next is None
        return stack


vals = [1, 2, 3, 4, 5]


print(Solution().reverseList(head))
