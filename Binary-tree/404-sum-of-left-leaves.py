class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Return 0 for an empty tree

        # Check if the left child is a leaf node
        if root.left and not root.left.left and not root.left.right:
            left_leaf_sum = root.left.val
        else:
            left_leaf_sum = 0

        # Recursively calculate the sum for both left and right subtrees
        left_leaf_sum += self.sumOfLeftLeaves(root.left)
        left_leaf_sum += self.sumOfLeftLeaves(root.right)

        return left_leaf_sum