# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val<=list2.val:
            next_node = list1.next
            list1.next = self.mergeTwoLists(next_node, list2)
            return list1
        else:
            next_node = list2.next
            list2.next = self.mergeTwoLists(list1, next_node)
            return list2
        

