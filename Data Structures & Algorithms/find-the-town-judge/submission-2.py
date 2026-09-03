class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing=[0]*(n+1)
        incoming=[0]*(n+1)
        for i in trust:
            outgoing[i[0]]+=1
            incoming[i[1]]+=1
        print("outgoing: ",outgoing)
        print("incoming: ",incoming)
        for i in range(n+1):
            if outgoing[i]==0 and incoming[i]==n-1:
                return i
        return -1


