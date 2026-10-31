# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKthNode(curr, k):
            while curr and k > 1:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = getKthNode(group_prev.next, k)
            if not kth:
                break
            group_next = kth.next
            group_head = group_prev.next
            prev = group_next
            curr = group_head
            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            group_prev.next = prev
            group_prev = group_head
        return dummy.next

            
        