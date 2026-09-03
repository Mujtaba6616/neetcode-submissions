class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        else:
            for i in range(len(s)):
                for j in range(len(t)):
                    if(s[i]==t[j]):
                        t=t[:j]+t[j+1:]
                        break

            if(len(t)!=0):
                return False
            else:
                return True                        
