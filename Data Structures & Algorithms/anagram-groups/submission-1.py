class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lsOfDic = {}
        lsAns = [] 
        for s in strs:
            if lsOfDic.get(self.addToMap(s)) is None:
                lsOfDic[self.addToMap(s)] = []
            lsOfDic[self.addToMap(s)].append(s)
        
        """ add the anagrams into a list """
        for val in lsOfDic.values():
            lsAns.append(val)
        return lsAns

    def addToMap(self, currStr: str) -> tuple:
        dic = {}
        for c in currStr:
            if dic.get(c) is None:
                dic[c] = 0
            dic[c] = dic[c] + 1
        return tuple(sorted(dic.items()))