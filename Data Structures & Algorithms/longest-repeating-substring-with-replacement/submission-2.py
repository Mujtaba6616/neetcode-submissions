class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map={}
        left=0
        count=0
        res=0
        for right in range(len(s)):
            hash_map[s[right]]=1+hash_map.get(s[right],0)
            if (right-left+1)-max(hash_map.values())>k:
                hash_map[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        
        return res
            

            