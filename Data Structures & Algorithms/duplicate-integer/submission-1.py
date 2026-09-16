class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = set()
        for item in nums:
            if item in m:
                return True
            m.add(item)
        return False