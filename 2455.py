# Average Value of Even Numbers That are Divisible by Three
# 7/17/2023 Author: Yaw Karikari Wiafe


class Solution:
    def averageValue(self, num: List[int])-> int:
        sum = 0
        count = 0

        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                count += 1
                sum += i
        try: 
            return round(sum/count)
        except ZeroDivisionError:
            return 0
