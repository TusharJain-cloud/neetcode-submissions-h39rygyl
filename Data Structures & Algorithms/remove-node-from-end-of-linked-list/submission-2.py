# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return head.next
        
        length = 1
        cur1, cur2 = head, head

        while cur1.next:
            cur1 = cur1.next
            length += 1

        node_to_remove = length - n

        if node_to_remove == 0:
            return head.next

        for i in range(node_to_remove - 1):
            cur2 = cur2.next
        
        cur2.next = cur2.next.next
        return head
        
        # dummy = ListNode(0, head)

        # left = dummy
        # right = head

        # while n > 0 and right:
        #     right = right.next
        #     n -= 1
        
        # while right:
        #     left = left.next
        #     right = right.next

        # left.next = left.next.next

        # return dummy.next
        