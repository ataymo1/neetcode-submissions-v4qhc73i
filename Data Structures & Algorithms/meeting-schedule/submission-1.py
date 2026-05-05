"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        heap = []
        for interval in intervals:
            start, end = interval.start, interval.end
            heapq.heappush(heap, (start, end))

        cur_time = 0
        
        while heap:
            start, end = heapq.heappop(heap)
            if start < cur_time:
                return False
            cur_time = end

        return True
