# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
done in 2 minutes
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        followingMap = set()
        if head is None:
            return False

        myHead = head
        while myHead.next and myHead not in followingMap: # to dziala, bo adresy obiektow (wskazniki) sa tutaj trzymane
            followingMap.add(myHead)
            myHead = myHead.next

        if myHead.next is None:
            return False

        return True