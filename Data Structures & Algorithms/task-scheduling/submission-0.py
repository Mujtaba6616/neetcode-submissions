class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic=Counter(tasks)
        max_h=[]
        for i in dic:
            heapq.heappush(max_h,-dic[i])
        time=0
        q=deque()
        while max_h or q:
            time+=1 
            if max_h:
                x=heapq.heappop(max_h)
                if x+1!=0:
                    q.append((x+1,time+n))
            if q and q[0][1]==time:
                y,z=q.popleft()
                heapq.heappush(max_h,y)
                
        
        return time     
