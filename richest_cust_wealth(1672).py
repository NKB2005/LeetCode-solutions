class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0

        for acc in accounts:
            cust_wealth = 0

            for num in acc:
                cust_wealth = cust_wealth + num

            if cust_wealth > max_wealth:
                max_wealth = cust_wealth

        return max_wealth