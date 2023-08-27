# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


### CYCLE in loop 

# Need to study tree rotations!


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            
            # Save the current node
            b = node
            
            # Update left subtree if needed
            if node.left and node.left.left and not node.right:
                c = node.left.left
                node.left = c
                node.right = b
                node.left.left = None  # Update left.left to None
                return node
            
            # Update right subtree if needed
            elif node.right and node.right.right and not node.left:
                c = node.right.right
                node.right = c
                node.left = b
                node.right.right = None  # Update right.right to None
                return node
            
            # Recursively update left and right subtrees
            if node.left and node.left.left:
                node.left = dfs(node.left)
            if node.right and node.right.right:
                node.right = dfs(node.right)
            
            return node  # Return the modified node
        
        return dfs(root)