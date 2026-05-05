class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        heap = []
        res = []

        for i, interval in enumerate(intervals):

            start, end = interval

            heapq.heappush(heap, (start, end))

        cur_start, cur_end = heapq.heappop(heap)
        
        while heap:
            next_start, next_end = heapq.heappop(heap)


            # check to see if new interval

            if next_start > cur_end:
                res.append([cur_start, cur_end])
                cur_start, cur_end = next_start, next_end
                continue
            
            cur_end = max(cur_end, next_end)

        res.append([cur_start, cur_end])
        return res
            
            
            
            

            
            
            
        