# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, node):
        if not node.next:
            return node
        new_head = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return new_head

    def reverse_iterative(self, head):
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        prev, cur = ListNode(0, head), head
        while cur and count<k:
            count += 1
            cur = cur.next
            prev = prev.next
        if count<k:
            return head
        next_node = cur
        prev.next = None
        reversed_node = self.reverse_iterative(head)
        head.next = self.reverseKGroup(next_node, k)
        return reversed_node
        


        