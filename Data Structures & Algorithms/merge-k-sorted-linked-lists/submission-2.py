# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            dummy = ListNode(0)
            current = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            current.next = list1 if list1 else list2
            return dummy.next

        if not lists:
            return None

        interval = 1
        k = len(lists)

        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])

            interval *= 2

        return lists[0]

        