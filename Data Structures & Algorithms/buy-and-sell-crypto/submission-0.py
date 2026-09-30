class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        top, min = 0, 100

        for val in prices:
            if val < min:
                min = val
            elif val > min and val-min > top:
                top = val-min

        return top