class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = {}

        for i, num in enumerate(nums):
            if target - num in hist: 
                return [hist.get(target - num), i]
            hist[num] = i