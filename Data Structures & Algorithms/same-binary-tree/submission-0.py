class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.store1 = []
        self.store2 = []
        
        def dfs(x, check):
            # 🔥 FIX: record structure when node is None
            if x is None:
                if check:
                    self.store1.append(None)
                else:
                    self.store2.append(None)
                return
            
            # You were doing postorder — keeping that same order
            dfs(x.left, check)
            dfs(x.right, check)
            
            if check:
                self.store1.append(x.val)
            else:
                self.store2.append(x.val)
        
        dfs(p, True)
        dfs(q, False)
        
        return self.store1 == self.store2