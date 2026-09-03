class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root == None:
            return False

        curr = root

        if curr.left == None and curr.right == None:
            return targetSum == curr.val

        return (
            self.hasPathSum(curr.left, targetSum - curr.val)
            or
            self.hasPathSum(curr.right, targetSum - curr.val)
        )