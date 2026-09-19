import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        zero = True
        for c in s:
            if c.isalnum():
                zero = False
                break
            
        if zero:
            return zero

        i, j = 0, len(s) - 1

        while i < j:
            while not s[i].isalnum() and i < len(s) - 1:
                i += 1
            while not s[j].isalnum() and j > 0:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else: 
                return False

        return True
            