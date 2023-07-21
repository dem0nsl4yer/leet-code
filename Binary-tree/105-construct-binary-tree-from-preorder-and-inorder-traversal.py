# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if inorder and preorder:
            k = preorder.pop(0)
            dummy = TreeNode(k)
            # find index of root node in inorder traversal 
            inorder_index = inorder.index(k)
            #inorder index - also gives number of elements in the left subtree. 
            dummy.left = self.buildTree(preorder, inorder[:inorder_index])
            dummy.right = self.buildTree(preorder, inorder[inorder_index + 1:])
            return dummy