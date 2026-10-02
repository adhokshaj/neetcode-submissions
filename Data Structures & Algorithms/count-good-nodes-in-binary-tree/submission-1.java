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
    public int goodNodes(TreeNode root) {
        int[] count = new int[1];
        dfs(root, root.val, count);
        return count[0];
    }
    private void dfs(TreeNode node, int prev_max, int[] count){
        if(node==null){
            return;
        }
        if(node.val>=prev_max){
            count[0] += 1;
            prev_max = node.val;
        }
        dfs(node.left, prev_max, count);
        dfs(node.right, prev_max, count);
    }
}
