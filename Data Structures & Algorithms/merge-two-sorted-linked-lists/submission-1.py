# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def usingPointeres(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
        
    def usingRecursion(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        ''' Now both lists are not empty
            1. Now we have list1 node and list2 node
            2. If list1 node is less that list2 node, we want
                the linkedlist thats merged till now to attach to 
                this node and return
            3. Else to list2's node do the same and return
        '''

        if list1.val <= list2.val:
            list1.next = self.usingRecursion(list1.next, list2)
            return list1
        else:
            list2.next = self.usingRecursion(list1, list2.next)
            return list2


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.usingRecursion(list1, list2)
        