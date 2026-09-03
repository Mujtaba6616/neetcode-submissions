class Solution:
    def isValid(self, s: str) -> bool:
        stack1=[]
        for ch in s:
            if ch in "({[":
                stack1.append(ch)
            else:

                if not stack1:
                    return False

                top=stack1.pop()
                if ch == ')' and top != '(':
                    return False
                elif ch == ']' and top != '[':
                    return False
                elif ch == '}' and top != '{':
                    return False

        return len(stack1) == 0
        
        
        
            
        

        