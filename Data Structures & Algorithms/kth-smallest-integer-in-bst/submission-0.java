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
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> st = new Stack<>();
        var cur = root;
        while(cur!=null || !st.isEmpty()){
            // System.out.println(st);
            while(cur != null){
                st.push(cur);
                cur = cur.left;
            }
            var top = st.pop();
            k -= 1;
            if(k==0){
                return top.val;
            }
            cur = top.right;
        }
        return -1;
    }
}
