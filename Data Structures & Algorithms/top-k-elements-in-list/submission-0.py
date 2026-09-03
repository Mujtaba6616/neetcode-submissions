
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        arr=[[] for i in range(len(nums)+1)]
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        for n,c in hashmap.items():
            arr[c].append(n)
        res=[]
        for i in range(len(nums),0,-1):
            for n in arr[i]:
                res.append(n)
                if(len(res)==k):
                    return res
            
                
            

        
        
           
                 