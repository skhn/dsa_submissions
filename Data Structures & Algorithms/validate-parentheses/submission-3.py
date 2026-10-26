class Solution:
    def isValid(self, s: str) -> bool:
        stck = deque()
        matcher = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in matcher:
                if not stck or matcher[c] != stck[-1]:
                    return False
                stck.pop()
            else:
                stck.append(c)
        return not stck
            


        

        