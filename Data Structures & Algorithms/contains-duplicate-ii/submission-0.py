class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=1
        while i<=len(nums)-1:
            while j<=len(nums)-1:
                if i!=j and nums[i]==nums[j] and abs(i-j)<=k:
                    return True
                j+=1
            j=0
            i+=1
        return False

