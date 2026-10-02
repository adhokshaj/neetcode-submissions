/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int max_sum = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        dfs(root);
        return max_sum;
    }

    private int dfs(TreeNode node){
        if (node==null){
            return 0;
        }
        int l = dfs(node.left);
        int r = dfs(node.right);
        max_sum = Math.max(max_sum, l+r+node.val);
        max_sum = Math.max(max_sum, l+node.val);
        max_sum = Math.max(max_sum, r+node.val);
        max_sum = Math.max(max_sum, node.val);
        return Math.max(node.val + Math.max(l,r), node.val);
    }
}
