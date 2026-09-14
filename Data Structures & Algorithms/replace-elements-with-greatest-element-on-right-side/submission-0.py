class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)):
            if i<len(arr)-1:
                ans.append(max(arr[i+1:]))
            else:
                ans.append(-1)
        return ans