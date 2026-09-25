# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if (not head) or (not head.next):
            return
        
        def findMid(node):
            s,f = node, node.next
            while f and f.next:
                s = s.next
                f = f.next.next
            res = s.next
            s.next = None
            return res
        
        def reverse(node):
            if not node.next:
                return node
            
            newHead = reverse(node.next)
            node.next.next = node
            node.next = None
            return newHead 


        mid_node = findMid(head)

        # reverse linkedList from mid to end
        end_node = reverse(mid_node)

        l,r = head, end_node

        while r:
            temp1, temp2 = l.next, r.next
            l.next = r
            r.next = temp1
            l = temp1
            r = temp2



        