class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        heap = []
        res = 0

        for start, end in intervals:
            heapq.heappush(heap, (start, end))

        
        cur_start, cur_end = heapq.heappop(heap)

        while heap:

            next_start, next_end = heapq.heappop(heap)

            if next_start >= cur_end:
                cur_start = next_start
                cur_end = next_end
            else:
                cur_end = min(cur_end, next_end)
                res += 1

        return res

        