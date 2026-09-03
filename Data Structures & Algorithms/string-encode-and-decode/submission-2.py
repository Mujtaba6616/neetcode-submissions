class Solution:

    def decode(self, s: str) -> List[str]:
        ans=[]
        temp=""
        for l in s:
            if(l!="`"):
                temp+=l
            else:
                ans.append(temp)
                temp=""
        return ans

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += word + "`"

        return encoded
        




                

