class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numdict = {}

        for i, num in enumerate(numbers, start = 1):
            if target - num in numdict:
                return [numdict[target-num], i]
            numdict[num] = i
            