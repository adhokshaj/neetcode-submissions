# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp = curr1.next
                curr1.next = None
                curr.next = curr1
                curr1 = temp
                curr = curr.next
            else:
                temp = curr2.next
                curr2.next = None
                curr.next = curr2
                curr2 = temp
                curr = curr.next
            
            
        
        if not curr1:
            curr.next = curr2
        else:
            curr.next = curr1

        return dummy.next
        