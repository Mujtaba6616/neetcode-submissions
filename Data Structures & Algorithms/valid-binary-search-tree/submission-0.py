class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(v):
            if v == None:
                return True, float('inf'), float('-inf')
            
            left_v, left_min, left_max = dfs(v.left)
            right_v, right_min, right_max = dfs(v.right)

            if not left_v or not right_v:
                return False, 0, 0

            if v.left and v.val <= left_max:
                return False, 0, 0

            if v.right and v.val >= right_min:
                return False, 0, 0

            return True, min(v.val, left_min), max(v.val, right_max)

        return dfs(root)[0]