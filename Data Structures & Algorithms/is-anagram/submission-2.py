class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.adict = dict()
        if len(s) != len(t):
            return False;
        for i in range(len(s)):
            self.adict.update({s[i]: self.adict.get(s[i],0)+1})
        for i in range(len(t)):
            self.adict.update({t[i]: self.adict.get(t[i],0)-1}) 
        return all(0 == val for val in self.adict.values())

        