class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set()

        for num in nums:
            nset.add(num)

        high = 0
        for num in nums:
            if num-1 not in nset:
                l = 0
                while num in nset:
                    num += 1
                    l += 1
                    print(num)
                if l > high:
                    high = l
        
        return high

