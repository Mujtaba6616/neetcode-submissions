class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=0
        stack=[]
        for i in tokens:
            if i.lstrip("-").isnumeric():
                stack.append(int(i))
                print(stack)
            else:
                n1=stack.pop()
                n2=stack.pop()
                if i == "+":
                    stack.append(n1+n2)
                elif i=="*":
                    stack.append(n1*n2)
                elif i=="-":
                    stack.append(n2-n1)
                elif i=="/":
                    stack.append(int(n2/n1))
                    
        return stack.pop()

                
        