# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head1, head2 = list1, list2
        dummy = ListNode()
        dummy.next = list1
        prevNode = dummy
        # im gonna add head2 nodes to head1 list
        if head1 is None:
            return head2
        elif head2 is None:
            return head1

        while head2 is not None:
            if head1 is not None and head1.val >= head2.val:
                t = head2
                head2 = head2.next
                t.next = head1
                prevNode.next = t
                prevNode = t
            elif head1.next is not None:
                prevNode = head1
                head1 = head1.next
            else:
                head1.next = head2
                return dummy.next

        return dummy.next
