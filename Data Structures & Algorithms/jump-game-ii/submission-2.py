class Solution:
    def jump(self, nums: List[int]) -> int:

        length = len(nums)
        if length == 1:
            return 0
        
        reachable_max = 0
        current_max = 0
        jumps = 0

        for i, n in enumerate(nums):
            reachable_max = max(reachable_max, n + i)
            
            if current_max >= length - 1:
                return jumps
            if reachable_max >= length - 1:
                return jumps + 1

            if current_max == i:
                jumps += 1
                current_max = reachable_max
            
            

        return jumps
            
            

            
            
        