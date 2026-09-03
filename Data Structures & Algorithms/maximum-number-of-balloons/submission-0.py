class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ct=Counter(text)
        bln=Counter("balloon")

        res=float('inf')
        for c in bln:
            res=min(res,ct[c]//bln[c])
            
        return res