class TimeMap:

    def __init__(self):

        # arr going to be stored as tuple(value, timestamp)
        self.h_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:


        if key not in  self.h_map:
            self.h_map[key] = [tuple((value, timestamp))]
            return
        
        cur_arr = self.h_map[key]
        for i in range(len(cur_arr)):
            if timestamp < cur_arr[i][1]:
                cur_arr.insert(i, tuple((value, timestamp)))
                return
        
        cur_arr.append(tuple((value, timestamp)))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.h_map:
            return ""

        cur_arr = self.h_map[key]

        #print(f"timestamp we want {timestamp} : \ncur arr :{cur_arr}")
        if cur_arr[0][1] > timestamp:
            return ""

        left = 0
        right = len(cur_arr)

        cur_value = cur_arr[0][0]

        while left < right:
            middle = (left + right) // 2
            middle_time = cur_arr[middle][1]
            #print(f"   {middle_time}")

            if middle_time > timestamp:
                right = middle 
            elif middle_time < timestamp:
                cur_value = cur_arr[middle][0]
                left = middle + 1
            else:
                return cur_arr[middle][0]
        
        return cur_value
            
        
