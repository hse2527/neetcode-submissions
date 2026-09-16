class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for val in nums:
            if val in dup:
                return True
            dup.add(val)
        return False
