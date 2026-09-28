class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(list1, list2):
            dummy = ListNode()
            curr = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next

                curr = curr.next

            curr.next = list1 if list1 else list2

            return dummy.next

        def dfs(left, right):
            if left == right:
                return lists[left]

            mid = (left + right) // 2

            left_list = dfs(left, mid)
            right_list = dfs(mid + 1, right)

            return merge(left_list, right_list)

        return dfs(0, len(lists) - 1)