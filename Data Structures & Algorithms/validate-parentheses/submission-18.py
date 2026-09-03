class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opening=['(','{','[']
        
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
                print("Before Pop:", stack)
            else:
                if stack and ((s[i]=="}" and stack[-1]=="{") or (s[i]==")" and stack[-1]=="(") or (s[i]=="]" and stack[-1]=="[")):
                    stack.pop()
                    print("After Pop:", stack)
                else:
                    return False

        if not stack:
            return True
        else:
            return False
        