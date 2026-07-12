class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c_ones = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
                if counter > c_ones:
                    c_ones = counter
            if num != 1:
                counter = 0
        return c_ones
            
            
        