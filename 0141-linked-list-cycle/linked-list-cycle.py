# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortise = head

        while hare and tortise:
            hare = hare.next
            if hare:
                hare = hare.next
            tortise = tortise.next

            if hare and tortise:
                if hare == tortise:
                    return True
            else: return False
        
        return False
        