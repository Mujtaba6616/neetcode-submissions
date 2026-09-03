class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        if len(points)==0:
            return ans.append([])
        minDist=float('inf')
        row=len(points)
        col=len(points[0])

        for i in points:
            dist=math.sqrt(i[0]**2 + i[1]**2)
            i.append(dist)
        
        points.sort(key=lambda x:x[2])
        for i in range(k):
            ans.append(points[i][:2])
        return ans
            
        

            


            
        