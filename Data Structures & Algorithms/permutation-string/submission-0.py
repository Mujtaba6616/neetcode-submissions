class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1={}
        for ch in s1:
            if ch not in freq1:
                freq1[ch]=0
            freq1[ch]+=1

        left=0
        window={}
        size=len(s1)
        for right in range(len(s2)):
            if(s2[right] not in window):
                window[s2[right]]=0
            window[s2[right]]+=1
            if(right-left+1>size):
                window[s2[left]]-=1
                if(window[s2[left]]==0):
                    del window[s2[left]]
                left+=1
            
            if(window==freq1):
                return True
        return False
                