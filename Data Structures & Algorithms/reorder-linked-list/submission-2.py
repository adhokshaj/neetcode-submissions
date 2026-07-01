# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(node):
            if not node:
                return node
            new_head = node
            if node.next:
                new_head = reverse(node.next)
                node.next.next = node
            node.next = None
            return new_head

        if not head or not head.next:
            return
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        tmp = s.next
        s.next = None
        second_part = reverse(tmp)
        l,r = head, second_part
        # while r:
        #     print(r.val)
        #     r = r.next

        while r:
            # print(l.val, r.val)
            tmp1= l.next
            tmp2 = r.next
            l.next = r
            r.next = tmp1
            l = tmp1
            r = tmp2