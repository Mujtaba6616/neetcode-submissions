class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        ans=[]
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                hashmap[nums[i]]+=1
        items=list(hashmap.items())
        items.sort(key=lambda x:x[1],reverse=True)
        for i in range(k):
            ans.append(items[i][0])
        return ans

        


        
        