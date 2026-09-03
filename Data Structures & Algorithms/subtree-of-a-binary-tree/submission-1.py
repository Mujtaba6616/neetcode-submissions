# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None:
            return False
        if self.check(root,subRoot)==True:
            return True 
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def check(self,p,q):
        if p==None and q==None:
            return True
        if p is None or q is None or p.val!=q.val:
            return False
        return self.check(p.left,q.left) and self.check(p.right, q.right)

   
        
        

