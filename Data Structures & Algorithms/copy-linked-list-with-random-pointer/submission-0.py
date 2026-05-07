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
        copyold = {None : None}

        curr = head
        while curr: 
            copy = Node(curr.val)
            copyold[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copyold[curr]
            copy.next = copyold[curr.next]
            copy.random = copyold[curr.random]
            curr = curr.next
        return copyold[head]