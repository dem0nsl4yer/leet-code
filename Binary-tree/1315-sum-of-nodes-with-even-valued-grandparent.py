# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0 
            val = 0  # Initialize val for the current node
            if node.val % 2 == 0:
                if node.left and node.left.left:
                    val += node.left.left.val
                if node.right and node.right.right:
                    val += node.right.right.val
                if node.right and node.right.left:
                    val += node.right.left.val
                if node.left and node.left.right:
                    val += node.left.right.val
            # Accumulate val 
            val += dfs(node.left)
            val += dfs(node.right)
            return val
        
        return dfs(root)  # Return the accumulated val from the entire tree
    

## cleaner solution with single iteration 

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def dfs(currentNode, parentValue, grandParentValue):
            subResult = 0 

            if grandParentValue % 2 == 0:
                subResult += currentNode.val

            if currentNode.left:
                subResult += dfs(currentNode.left, currentNode.val, parentValue)

            if currentNode.right:
                subResult += dfs(currentNode.right, currentNode.val, parentValue)

            return subResult
        
        return dfs(root,-1,-1)