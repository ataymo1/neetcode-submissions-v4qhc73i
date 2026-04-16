class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        strength = 0
        
        for i, n in enumerate(nums):
            strength = max(n, strength)
            if strength == 0:
                if i == len(nums) - 1:
                    return True
                return False
            strength -= 1
        
        return True
        

            
            
            