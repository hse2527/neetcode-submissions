class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solMap = {}

        for cur in strs:
            key = tuple(sorted(cur))
            solMap.setdefault(key,[]).append(cur)
        
        return list(solMap.values())