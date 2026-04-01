class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        cache = dict()
        def dp(i, sum1, sum2):
            index = tuple((i, sum1, sum2))
            index2 = tuple((i, sum2, sum1))
            if index in cache:
                return cache[index]
            if index2 in cache:
                return cache[index2]
            
            if i == len(stones):
                return abs(sum1 - sum2)
            
            cache[index] = min(dp(i+1, sum1 + stones[i], sum2), dp(i+1, sum1, sum2 + stones[i]))
            cache[index2] = cache[index]
            
            return cache[index]
            
        return dp(0, 0, 0)
                    

                


