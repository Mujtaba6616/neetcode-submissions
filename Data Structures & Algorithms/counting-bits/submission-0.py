class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        count=0
        res.append(0)
        for i in range(1,n+1):
            while i:
                count+=i%2
                i=i>>1
            res.append(count)
            count=0

        return res
        