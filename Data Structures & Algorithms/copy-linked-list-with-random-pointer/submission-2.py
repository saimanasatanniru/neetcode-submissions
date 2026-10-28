"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy = {}
        curr = head

        #cope the values first later we will copy the links
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy_node = copy[curr]
            copy_node.next = copy[curr.next] if curr.next else None
            copy_node.random = copy[curr.random] if curr.random else None
            curr = curr.next
        return copy[head]
        