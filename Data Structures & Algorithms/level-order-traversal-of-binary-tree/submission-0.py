# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        ans=[]
        if root:
            queue.append(root)
        while queue:
            size=len(queue)
            lvl=[]
            for i in range(size):
                item=queue.pop(0)
                lvl.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)

            
            ans.append(lvl)
        return ans



        