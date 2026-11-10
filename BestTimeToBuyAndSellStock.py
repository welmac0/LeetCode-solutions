class Solution:
    """
    Done in like 5 minutes, no hints. O(n)
    """

    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = L
        bestPrice = -float("inf")
        while R < len(prices):
            price = prices[R] - prices[L]
            if price < 0:
                L = R
                R = min(len(prices) - 1, L + 1)
            else:
                bestPrice = max(price, bestPrice)
                R += 1

        return bestPrice
