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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        
        return build(0, 0, inorder.length -1, preorder, inorder);

    }

    public TreeNode build(int pStart, int inStart, int inEnd, int [] preorder, int [] inorder){

        if(pStart > preorder.length - 1 || inStart > inEnd)
            return null;

        TreeNode root = new TreeNode(preorder[pStart]);
        int inIndex = inStart;
        
        while(inIndex < inEnd){
            if(preorder[pStart] == inorder[inIndex])
                break;
            
            inIndex++;
        }

        root.left = build(pStart + 1, inStart, inIndex - 1, preorder, inorder);
        root.right = build(pStart + inIndex - inStart + 1, inIndex + 1, inEnd, preorder, inorder);

        return root;
        

    }
}