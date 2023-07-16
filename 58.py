#Length of Last word
#7/16/2023 Author: Yaw Karikari Wiafe
class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        return len(s.strip().split(' ')[-1])
