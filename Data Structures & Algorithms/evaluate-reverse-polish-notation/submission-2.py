class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t.lstrip('-').isnumeric():
                stack.append(int(t))
            else:
                p1 = stack.pop()
                p2 = stack.pop()
                
                if t == "+":
                    stack.append(p2 + p1)
                elif t == "-":
                    stack.append(p2 - p1)
                elif t == "*":
                    stack.append(p2 * p1)
                elif t == "/":
                    stack.append(int(p2 / p1))
        
        return stack.pop()
