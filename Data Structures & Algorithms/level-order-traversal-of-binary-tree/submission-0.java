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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if(root==null){
            return ans;
        }
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        

        while(!q.isEmpty()){
            // q.stream().forEach(n->System.out.print(n.val));
            // System.out.println();
            List<Integer> level = new ArrayList<>();
            int level_len = q.size();
            while(level_len>0){
                var node = q.poll();
                level.add(node.val);
                if(node.left != null){
                    q.offer(node.left);
                }
                if(node.right != null){
                    q.offer(node.right);
                }
                level_len -= 1;
            }
            ans.add(level);
        }

        return ans;
        
    }
}
