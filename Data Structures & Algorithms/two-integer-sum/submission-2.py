class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums=sorted(nums)
        left=0
        right=len(sorted_nums)-1
        ans=[]
        ret=[]
        while left<right:
            if(sorted_nums[left]+sorted_nums[right]<target):
                left+=1
            elif(sorted_nums[left]+sorted_nums[right]>target):
                right-=1
            else:
                ans.append(left)
                ans.append(right)
                break
        l=ans[0]
        r=ans[1]
        for i in range(len(nums)):
            if(sorted_nums[l]==nums[i]):
                ret.append(i)
            elif(sorted_nums[r]==nums[i]):
                ret.append(i)
        return ret






                
