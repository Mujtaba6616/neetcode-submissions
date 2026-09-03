class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        ans=[]
        while l<r:
            if numbers[l]+numbers[r]<target:
                l+=1
                print("l",l)
            elif numbers[l]+numbers[r]>target:
                r=r-1
                print("r",r)
            else:
                ans.append(l+1)
                ans.append(r+1)
                break
            
        return ans
        