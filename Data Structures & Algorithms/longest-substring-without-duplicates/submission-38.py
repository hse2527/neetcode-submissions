class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, cur, top = 0, 0, 0
        cset = set()

        while cur < len(s):
            ch = s[cur]
            if ch in cset:
                top = max(cur - start,top)
                while start < cur:
                    sch = s[start]
                    start += 1
                    cset.remove(sch)

                    if ch == sch:
                        break
            
            cset.add(ch)
            cur += 1

        return max(top,cur - start)