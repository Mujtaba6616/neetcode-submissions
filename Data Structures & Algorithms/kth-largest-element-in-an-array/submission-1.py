import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[]
        for i in range(len(nums)):
            heapq.heappush(max_heap,-nums[i])
        for i in range(k):
            ans=-heapq.heappop(max_heap)
        return ans


