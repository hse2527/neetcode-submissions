class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        imap = {}

        for num in nums:
            if num in imap:
                continue
            prev = imap.get(num - 1,[num,num])
            post = imap.get(num + 1,[num,num])
                
            val = [prev[0], post[1]]
            imap[num] = val
            imap[prev[0]] = val
            imap[post[1]] = val
            
        high = 1
        for init, fin in imap.items():
            cur = fin[1] - init
            if cur >= high:
                high = cur + 1

        return high


        