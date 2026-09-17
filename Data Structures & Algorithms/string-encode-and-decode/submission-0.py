class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            l = len(s)
            f = f"{l:03d}"
            out = out+ f + s
        return out


    def decode(self, s: str) -> List[str]:
        sol = []
        while s:
            l = int(s[:3])
            sol.append(s[3:3+l])
            s = s[3+l:]
        return sol


