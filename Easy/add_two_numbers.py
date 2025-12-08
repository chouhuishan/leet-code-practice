# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # num1 = "".join([str(i) for i in l1][::-1])
        # num2 = "".join([str(i) for i in l2][::-1])
        # res = int(num1) + int(num2)
        # res = list(map(int, str(res)))
        # return res[::-1]

        head = ListNode(0)
        current = head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            col_sum = l1_val + l2_val + carry
            carry = col_sum // 10
            new_digit = col_sum % 10

            current.next = ListNode(new_digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return head.next


# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# l1 = [0]
# l2 = [0]
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
print(Solution().addTwoNumbers(l1, l2))
