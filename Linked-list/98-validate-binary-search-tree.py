# Definition for a binary tree node.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(node, minA, maxA):
            if node is None:
                return True
            
            # Check if the current node's value is within the range of its parent node
            # every node has its own min and max

            if not minA < node.val < maxA:
                return False

            # Recursively check left and right subtrees with updated ranges
            return (isValidBSTHelper(node.left, minA, node.val) and 
                    isValidBSTHelper(node.right, node.val, maxA))
        # split here defines that left node is going to have maximum possible value of node parent. Then min will come from the key upwards. 
        # simialrly, for right node, additional qualifer is the minimum possible value which is its parent. 
        # Recursion works best, as in every iteration we are adding a layer of constraints, be it right.left or left.right etc. 
        # A new function had to be defined, due to the rise in arguments, wrt the original function. 
        return isValidBSTHelper(root, float('-inf'), float('inf'))


##working solution - 



# Doesn't works, as we are unable to keep track of the root here due to the dynamic situation. 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left = root.left
        right = root.right
        if left is None and right is None:
            return True
        elif left is None or right is None:
            if right:
                return  right.val > root.val and self.isValidBST(root.right)
            if left:
                return  left.val < root.val  and self.isValidBST(root.left)
        elif right.val > root.val and  left.val < root.val:
            return self.isValidBST(left) and self.isValidBST(right)
        return False