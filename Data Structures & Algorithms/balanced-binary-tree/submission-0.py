# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check=True
        def dfs(curr,check):
            if curr==None:
                return 0
            l=dfs(curr.left,self.check)
            r=dfs(curr.right,self.check)
            if abs(l-r)>1:
                self.check=False
            return 1+max(l,r)
        dfs(root,self.check)
        return self.check
        