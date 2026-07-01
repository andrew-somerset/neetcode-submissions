class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_ones = 0
        max_consecutive_ones = 0
        for i in nums:
            if i == 1:
                consecutive_ones += 1
            else:
                consecutive_ones = 0
            if max_consecutive_ones < consecutive_ones:
                max_consecutive_ones = consecutive_ones
            else:
                continue
        return max_consecutive_ones
            
        