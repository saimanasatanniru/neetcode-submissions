# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #why dummy node because the node that we need to remove is head itself then it will be safe to point dummy at beginning
        dummy = ListNode(0, head)
        left = dummy
        right = head
         #move right to n time to maintain the gap of n
        for _ in range(n):
            right = right.next

        #this makes us point the left correctly to the point before the node that we need to remove
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
        