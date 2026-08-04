# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # print(left, right)
            nonlocal maxx
            maxx = max(node.val, node.val + right+ left, node.val+right, node.val + left, maxx)
            return max(0,node.val + max(left, right))
        dfs(root)
        return maxx

        