"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times=[]

        for interval in intervals:
            start = interval.start
            end = interval.end
            times.append((start, 0))
            times.append((end, 1))
        
        times.sort(key=lambda x:(x[0], -x[1]))

        room=0
        max_room =0
        for time, event in times:
            if event ==0:
                room+=1
                max_room = max(max_room, room)
            else:
                room -=1
        return max_room