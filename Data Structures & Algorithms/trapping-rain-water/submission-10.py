class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        total, rtop, ltop = 0,0,0

        while l < r:
            rcur, lcur = height[r], height[l]
            rtop = max(rcur, rtop)
            ltop = max(lcur, ltop)

            total = total + (rtop - rcur) + (ltop - lcur)

            if rtop > ltop:
                l += 1
            elif ltop >= rtop:
                r -= 1
            
        return total