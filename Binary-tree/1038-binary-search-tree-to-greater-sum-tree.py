# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, sumt):
            if not node:
                return sumt
            right_sum = dfs(node.right, sumt)
            node.val += right_sum
            left_sum = dfs(node.left, node.val)

## Key thing is to take into account of the left children of right sub-tree. Hence, we need the left_sum as the final return for parent value. 
            return left_sum
        dfs(root, 0)
        return root
    

## Another solution: --> SLOWER

## Due to class instantiation and method calls. 

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cur_sum = 0 
        def traverse(node):
            if node:
                traverse(node.right)
                self.cur_sum += node.val
                node.val = self.cur_sum
                traverse(node.left)
        traverse(root)
        return root


## Making it faster by avoiding class instantiation  - using global var. 

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(node):
            nonlocal total
            if node:
                traverse(node.right)  # Traverse right subtree
                total += node.val
                node.val = total  # Update node's value
                traverse(node.left)  # Traverse left subtree
        
        total = 0  # Initialize the total sum
        traverse(root)  # Start the optimized in-order traversal
        return root  # Return the modified tree