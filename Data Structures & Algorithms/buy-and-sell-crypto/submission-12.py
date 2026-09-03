class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        ans=0
        while r<len(prices):
            if prices[l]<=prices[r]:
                if ans<prices[r]-prices[l]:
                    ans=prices[r]-prices[l]
                
            elif prices[l]>prices[r]:
                l=r
            r+=1
                
        return ans

        