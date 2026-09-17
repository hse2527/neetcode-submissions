class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        countm = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            d[i] = d.get(i,0) + 1
        

        for key, val in d.items():
            countm[val].append(key)

        sol = []
        for i in range(len(countm)-1, -1, -1):
            for num in countm[i]:
                sol.append(num)
            k -= len(countm[i])
            if k == 0:
                break
        return sol

