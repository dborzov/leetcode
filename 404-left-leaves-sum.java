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
     private class Item {
             TreeNode g;
             boolean leftie;
             Item(TreeNode x,boolean l) { g=x; leftie=l;}
     }

     public int sumOfLeftLeaves(TreeNode root) {
         int sum = 0;
         List<Item> stack = new ArrayList<>();
         stack.add(new Item(root, false));
         while (stack.size() != 0) {
             Item cur = stack.get(stack.size()-1);
             stack.remove(stack.size()-1);
             if (cur.g==null) { continue; }
             if ((cur.leftie) && (cur.g.left==null) && (cur.g.right==null)) { sum += cur.g.val; }
             stack.add(new Item(cur.g.right, false)); stack.add(new Item(cur.g.left, true));
         }
         return sum;
     }

 }
