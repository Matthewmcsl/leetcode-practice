from ast import List


class Solution:
    def maxProfit_slow(self, prices: List) -> int:
        """
        Terrible O(n^2) solution, exceeded time limit, but first try
        """
        biggest_profit = 0

        for buy_day in range(len(prices)):
            for sell_day in range(buy_day + 1, len(prices)):
                # no profit only loss, we skip
                if prices[sell_day] < prices[buy_day]:
                    continue
                else:
                    cur_profit = prices[sell_day] - prices[buy_day]
                    biggest_profit = max(biggest_profit, cur_profit)
        return biggest_profit
