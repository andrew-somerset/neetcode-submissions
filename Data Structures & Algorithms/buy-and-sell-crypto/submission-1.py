class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        margin = 0
        maxx = 0
        minn = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > maxx:
                maxx = prices[i]
                if maxx - minn > margin:
                    margin = maxx - minn
            if prices[i] < minn:
                minn = prices[i]
                maxx = 0
        return margin







        