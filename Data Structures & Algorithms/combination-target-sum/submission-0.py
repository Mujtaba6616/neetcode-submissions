class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)==0:
            return ans.append([])
        ans=[]
        subset=[]
        def backtrack(i,subset):
            if sum(subset)==target and subset not in ans:
                ans.append(subset.copy())
                return
            if i==len(nums) or sum(subset)>target:
                return

            subset.append(nums[i])
            backtrack(i,subset)
            subset.pop()
            backtrack(i+1,subset)

        backtrack(0,subset)
        return ans


        