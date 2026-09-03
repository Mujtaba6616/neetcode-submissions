"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start=[]
        end=[]
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        start.sort()
        end.sort()
        s=0
        e=0
        count=0
        maxCount=0
        while s<len(start):
            if start[s]<end[e]:
                count+=1
                s+=1
            elif start[s]>=end[e]:
                count-=1
                e+=1
            if maxCount<=count:
                maxCount=count
        return maxCount
             




        