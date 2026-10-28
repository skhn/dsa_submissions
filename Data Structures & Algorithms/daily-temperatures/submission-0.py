class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stc = []

        for i in range(n):
            while stc and temperatures[i] > temperatures[stc[-1]]:
                pop_idx = stc.pop()
                res[pop_idx] = i - pop_idx
            stc.append(i)
        return res
        