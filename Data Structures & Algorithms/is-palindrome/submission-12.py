class Solution:
    def isPalindrome(self, s: str) -> bool:
        final=s.lower()
        final = final.strip()
        x=0
        a=""
        for i in range(len(final)):
            if final[i].isalpha() or final[i].isalnum():
                a+=final[i]

        j=len(a)-1
        while(x<j):
            if a[x]!=a[j]:
                return False
            x+=1
            j-=1
        return True