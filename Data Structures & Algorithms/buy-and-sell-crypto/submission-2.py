class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        margin = 0
        minn = prices[0]
        for price in prices:
            minn = min(minn, price)
            margin = max(margin, price - minn)
        return margin








        