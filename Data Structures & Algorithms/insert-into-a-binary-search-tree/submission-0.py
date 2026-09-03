class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        curr = root

        if curr.val >= val:
            curr.left = self.insertIntoBST(curr.left, val)

        elif curr.val < val:
            curr.right = self.insertIntoBST(curr.right, val)

        return curr