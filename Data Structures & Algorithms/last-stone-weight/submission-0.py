import heapq
class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_h=[]
        for i in stones:
            max_h.append(-1*i)

        heapq.heapify(max_h)
        while len(max_h)>1:
            l1=-heapq.heappop(max_h)
            l2=-heapq.heappop(max_h)
            if l1-l2 > 0:
                heapq.heappush(max_h,-(l1-l2))
            elif l1-l2<0:
                heapq.heappush(max_h,-(l2-l1))
        
        if len(max_h)==0:
            return 0
        else:
            return -max_h[0]


        