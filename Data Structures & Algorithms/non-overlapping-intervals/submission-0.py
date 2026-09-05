class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[1])
        pre_end=intervals[0][1]
        count=0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < pre_end:
                count+=1
            else:
                pre_end = end
        return count
