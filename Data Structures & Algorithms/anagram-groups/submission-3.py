class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            entry = ','.join(sorted(s))
            if entry in mapping:
                mapping[entry].append(s)
            else:
                mapping[entry] = [s]
        return list(mapping.values())