/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 public class Solution {
     public List<List<Integer>> levelOrder(TreeNode root) {
       List<List<Integer>> res = new ArrayList<>();
       if (root==null) {return res; }
       List<TreeNode> stack = new ArrayList<TreeNode>(); stack.add(root);
       List<Integer> stackLev = new ArrayList<Integer>(); stackLev.add(0);
       while (stack.size() != 0) {
         TreeNode cur = stack.get(stack.size()-1);
         stack.remove(stack.size()-1);
         Integer level =  stackLev.get(stackLev.size()-1);
         stackLev.remove(stackLev.size()-1);

         if (res.size()==level) {res.add( new ArrayList<Integer>() ); }
         res.get(level).add( cur.val );
         if (cur.right!=null) { stack.add(cur.right); stackLev.add(level+1); }
         if (cur.left!=null) { stack.add(cur.left); stackLev.add(level+1); }
       }
       return res;

     }
 }
