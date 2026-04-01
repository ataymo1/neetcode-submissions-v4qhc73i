class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2


        cache = dict()
        
        def dp(i, total):
            index = tuple((i, total))
            if i == len(stones) or total >= target:
                return abs(total - (stoneSum - total))
            
            if index in cache:
                return cache[index]
            
            cache[index] = min(dp(i+1, total), dp(i+1, total + stones[i]))

            return cache[index]
            
        return dp(0, 0)
                    

                


