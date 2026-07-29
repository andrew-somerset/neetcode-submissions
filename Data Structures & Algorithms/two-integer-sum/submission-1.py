class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Val_Index = {}
        for i in range(len(nums)):
            if target - nums[i] in Val_Index:
                return [Val_Index[target - nums[i]], i]
            else:
                Val_Index[nums[i]] = i
