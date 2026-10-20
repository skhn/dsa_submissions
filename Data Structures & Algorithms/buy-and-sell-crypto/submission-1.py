class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans: int = 0
        if len(prices) == 1:
            return ans
        ptrl: int = prices[0]
        i: int = 1
        while i < len(prices):
            ptrr: int = prices[i]
            if ptrl < ptrr and ans < ptrr - ptrl:
                ans = ptrr - ptrl
            elif ptrl > ptrr:
                ptrl = prices[i]
            i += 1
        return ans