class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alph = [0] * 26

        for i, ch in enumerate(s):
            alph[ord(ch) - ord('a')] += 1
            alph[ord(t[i]) - ord('a')] -= 1

        for i, val in enumerate(alph):
            if val > 0:
                return False
        
        return True

