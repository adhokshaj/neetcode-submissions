# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, maxx):
            nonlocal ans
            if not node:
                return
            # print(node.val, maxx)
            if node.val>=maxx:
                ans += 1
            
            dfs(node.left, max(node.val, maxx))
            dfs(node.right, max(node.val, maxx))

            return

        dfs(root, float('-inf'))
        return ans