class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change = defaultdict(int)

        for bill in bills:
            if bill == 10:
                if change[5] < 1:
                    return False
                else:
                    change[5] -= 1
                    change[10] += 1
            elif bill == 20:
                if change[10] < 1:
                    if change[5] < 3:
                        return False
                    else:
                        change[5] -= 3
                else:
                    if change[5] < 1:
                        return False
                    change[10] -= 1
                    change[5] -= 1
            else:
                change[5] += 1
        
        return True

        