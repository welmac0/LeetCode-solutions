# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
done in like 10 minutes.
Becomes super easy once i realised the Horner pattern to dissasemble numbers :D
"""

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def getNumberFromNodes(l):
            head = l
            totalNum = 0
            counter = 0
            while head:
                totalNum += pow(10, counter) * head.val
                counter += 1
                head = head.next

            return totalNum

        def getListFromNumber(number):
            numS = str(number)  # 975

            head = None
            for c in numS:
                t = ListNode(val=c, next=head)
                head = t

            return head

        # 1 + 2*10 + 3*100
        num1 = getNumberFromNodes(l1)
        num2 = getNumberFromNodes(l2)
        total = num1 + num2
        return getListFromNumber(total)
