class Solution:
    def maxArea(self, heights: List[int]) -> int:

        a,b = 0, len(heights)-1
        sol = 0

        while a < b:
            y = b - a
            h = min(heights[a],heights[b])
            s = y*h
            sol = max(s,sol)

            if heights[a] <= heights[b]:
                a += 1
            elif heights[a] > heights[b]:
                b -= 1

        return sol
