class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, cur, l, top = 0, 0, 0, 0
        cset = set()

        while cur < len(s):
            ch = s[cur]
            if ch in cset:
                top = max(l,top)
                while start < cur:
                    l -= 1
                    sch = s[start]
                    start += 1
                    cset.remove(sch)

                    if ch == sch:
                        break
            
            cset.add(ch)
            cur += 1
            l += 1

        return max(top,l)