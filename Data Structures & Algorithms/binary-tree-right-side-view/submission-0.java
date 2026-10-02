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
    int prev_max_h = 0;
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        dfs(root,1, ans);
        return ans;
    }
    private void dfs(TreeNode node, int h, List<Integer> ans){
        if (node==null){
            return;
        }
        if (h>prev_max_h){
            prev_max_h = h;
            ans.add(node.val);
        }
        dfs(node.right, h+1, ans);
        dfs(node.left, h+1, ans);
    }
}
