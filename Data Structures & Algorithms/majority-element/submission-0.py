class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==0:
            return None
        hashMap={}
        n=len(nums)
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]]=1
            hashMap[nums[i]]+=1
        for num,freq in hashMap.items():
            if freq>n/2:
                return num

